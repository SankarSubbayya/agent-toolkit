import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from scraper import scrape_url, save_scraped_pages
from agent import create_agent_with_datastore, upload_documents, query_agent

st.set_page_config(page_title="Agent Toolkit", page_icon="🔍", layout="wide")
st.title("Agent Toolkit")
st.caption("Scrape any website with Apify, then chat with it using Contextual AI")

# --- Session state ---
if "agent_id" not in st.session_state:
    st.session_state.agent_id = None
    st.session_state.datastore_id = None
    st.session_state.conversation_id = None
    st.session_state.messages = []
    st.session_state.scraped = False

# --- Sidebar: Scrape ---
with st.sidebar:
    st.header("1. Scrape a Website")
    url = st.text_input("URL to scrape", placeholder="https://example.com")
    max_pages = st.slider("Max pages to crawl", 1, 50, 5)

    if st.button("Scrape & Index", type="primary", disabled=st.session_state.scraped):
        if not url:
            st.error("Please enter a URL")
        else:
            with st.status("Working...", expanded=True) as status:
                st.write("Scraping website with Apify...")
                items = scrape_url(url, max_pages=max_pages)
                st.write(f"Scraped {len(items)} pages")

                st.write("Saving pages...")
                paths = save_scraped_pages(items)
                st.write(f"Saved {len(paths)} documents")

                st.write("Creating Contextual AI agent...")
                agent_id, datastore_id = create_agent_with_datastore(
                    name=f"Research: {url[:50]}"
                )
                st.session_state.agent_id = agent_id
                st.session_state.datastore_id = datastore_id

                st.write("Uploading documents to datastore...")
                upload_documents(datastore_id, paths)

                st.session_state.scraped = True
                status.update(label="Ready to chat!", state="complete")

    if st.session_state.scraped:
        st.success("Website indexed! Ask questions in the chat.")
        if st.button("Reset"):
            for key in ["agent_id", "datastore_id", "conversation_id", "messages", "scraped"]:
                del st.session_state[key]
            st.rerun()

# --- Chat ---
if st.session_state.scraped:
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if msg.get("attributions"):
                with st.expander("Sources"):
                    for attr in msg["attributions"]:
                        st.markdown(f"- **{attr['source']}**: {attr['text'][:200]}")

    if prompt := st.chat_input("Ask a question about the scraped content..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                result = query_agent(
                    st.session_state.agent_id,
                    prompt,
                    st.session_state.conversation_id,
                )
                st.session_state.conversation_id = result["conversation_id"]
                st.markdown(result["answer"])
                if result["attributions"]:
                    with st.expander("Sources"):
                        for attr in result["attributions"]:
                            st.markdown(f"- **{attr['source']}**: {attr['text'][:200]}")

        st.session_state.messages.append({
            "role": "assistant",
            "content": result["answer"],
            "attributions": result["attributions"],
        })
else:
    st.info("Enter a URL in the sidebar and click 'Scrape & Index' to get started.")
