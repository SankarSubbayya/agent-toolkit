"""MCP server for the web-researcher OpenClaw skill.

Tools:
  - web_research_scrape: Scrape a URL with Apify
  - web_research_index: Upload scraped content to Contextual AI
  - web_research_query: Ask questions about indexed content
  - web_research_status: Check current research state
"""

import os
import json
import tempfile
from pathlib import Path

from mcp.server.fastmcp import FastMCP
from apify_client import ApifyClient
from contextual import ContextualAI

mcp = FastMCP("web-researcher")

# In-memory state for the current research session
state = {
    "scraped_items": [],
    "file_paths": [],
    "agent_id": None,
    "datastore_id": None,
    "conversation_id": None,
    "source_url": None,
}


def _get_apify_client() -> ApifyClient:
    return ApifyClient(os.environ["APIFY_API_TOKEN"])


def _get_contextual_client() -> ContextualAI:
    return ContextualAI(api_key=os.environ["CONTEXTUAL_API_KEY"])


@mcp.tool()
def web_research_scrape(url: str, max_pages: int = 5) -> str:
    """Scrape a website using Apify's Website Content Crawler.

    Args:
        url: The URL to scrape
        max_pages: Maximum number of pages to crawl (default 5, max 50)
    """
    max_pages = min(max_pages, 50)

    client = _get_apify_client()
    run_input = {
        "startUrls": [{"url": url}],
        "maxCrawlPages": max_pages,
        "crawlerType": "cheerio",
    }

    run = client.actor("apify/website-content-crawler").call(run_input=run_input)
    items = list(client.dataset(run["defaultDatasetId"]).iterate_items())

    # Save to temp files for later upload
    output_dir = tempfile.mkdtemp(prefix="web_researcher_")
    paths = []
    for i, item in enumerate(items):
        title = item.get("title", f"page_{i}")
        text = item.get("text", "")
        if not text:
            continue

        safe_name = "".join(c if c.isalnum() or c in " -_" else "_" for c in title)[:80]
        path = os.path.join(output_dir, f"{safe_name}.txt")
        with open(path, "w") as f:
            f.write(f"Title: {title}\n")
            f.write(f"URL: {item.get('url', 'N/A')}\n\n")
            f.write(text)
        paths.append(path)

    state["scraped_items"] = items
    state["file_paths"] = paths
    state["source_url"] = url

    return json.dumps({
        "status": "success",
        "pages_scraped": len(items),
        "documents_saved": len(paths),
        "source_url": url,
        "page_titles": [item.get("title", "Untitled") for item in items[:10]],
    })


@mcp.tool()
def web_research_index(name: str = "") -> str:
    """Upload scraped content to Contextual AI and create a research agent.

    Args:
        name: Optional name for the research agent
    """
    if not state["file_paths"]:
        return json.dumps({"status": "error", "message": "No scraped content found. Run web_research_scrape first."})

    client = _get_contextual_client()

    agent_name = name or f"Research: {state['source_url'][:50]}"

    # Create datastore first, then agent with that datastore
    ds = client.datastores.create(name=f"ds-{agent_name[:40]}")
    datastore_id = ds.id

    result = client.agents.create(
        name=agent_name,
        datastore_ids=[datastore_id],
        system_prompt=(
            "You are a research assistant. Answer questions based on the documents "
            "provided. Always cite your sources. If you don't know the answer from "
            "the provided documents, say so clearly."
        ),
    )

    agent_id = result.id

    for path in state["file_paths"]:
        client.datastores.documents.ingest(
            datastore_id=datastore_id,
            file=Path(path),
        )

    state["agent_id"] = agent_id
    state["datastore_id"] = datastore_id

    return json.dumps({
        "status": "success",
        "agent_id": agent_id,
        "datastore_id": datastore_id,
        "documents_indexed": len(state["file_paths"]),
        "agent_name": agent_name,
    })


@mcp.tool()
def web_research_query(question: str) -> str:
    """Ask a question about the scraped and indexed content.

    Args:
        question: The question to ask about the indexed web content
    """
    if not state["agent_id"]:
        return json.dumps({"status": "error", "message": "No agent created yet. Run web_research_scrape then web_research_index first."})

    client = _get_contextual_client()

    messages = [{"role": "user", "content": question}]
    kwargs = {"messages": messages}
    if state["conversation_id"]:
        kwargs["conversation_id"] = state["conversation_id"]

    response = client.agents.query.create(agent_id=state["agent_id"], **kwargs)

    state["conversation_id"] = str(response.conversation_id)

    attributions = []
    for a in (response.attributions or []):
        attr = {}
        if hasattr(a, "source_title"):
            attr["source"] = a.source_title
        if hasattr(a, "attributed_text"):
            attr["text"] = a.attributed_text
        if attr:
            attributions.append(attr)

    return json.dumps({
        "status": "success",
        "answer": response.message.content,
        "conversation_id": state["conversation_id"],
        "attributions": attributions,
    })


@mcp.tool()
def web_research_status() -> str:
    """Check the current state of the web researcher."""
    return json.dumps({
        "source_url": state["source_url"],
        "pages_scraped": len(state["scraped_items"]),
        "documents_indexed": len(state["file_paths"]),
        "agent_active": state["agent_id"] is not None,
        "agent_id": state["agent_id"],
        "conversation_active": state["conversation_id"] is not None,
    })


if __name__ == "__main__":
    mcp.run(transport="stdio")
