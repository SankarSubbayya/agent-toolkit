# Demo Script — Web Researcher (10 minutes)

---

## 1. The Problem (~2 min)

**Open with this:**

> "Raise your hand if you've ever spent 30 minutes reading through a documentation site just to find one answer."

**The pain:**

- Developers and researchers constantly need to understand new tools, APIs, and codebases
- Documentation is scattered across dozens of pages — you can't just Ctrl+F your way to an answer
- If you copy-paste docs into ChatGPT, you lose citations, you hit context limits, and the model halluccinates details
- There's no quick way to turn a live website into a reliable, queryable knowledge base

**The gap:**

> "What if you could point an AI agent at any website and immediately start asking it questions — and every answer came with citations back to the exact source page?"

**Transition:**

> "That's what we built. Web Researcher is an OpenClaw skill that scrapes any website and turns it into a grounded knowledge base you can chat with."

---

## 2. Your Tech Stack (~3 min)

**Show the architecture diagram (draw on whiteboard or show slide):**

```
User question → Apify (scrape) → Contextual AI (index + RAG) → Cited answer
```

**Apify — The data layer:**

> "Apify is our web scraping engine. We use their Website Content Crawler actor, which handles JavaScript rendering, pagination, and link following. You give it a URL and a page limit — it gives you clean, structured text from every page it finds."

> "Without Apify, we'd be writing our own crawler, dealing with rate limits, JS rendering, and anti-bot protections. That's not a hackathon project — that's a month of work."

**Contextual AI — The intelligence layer:**

> "Contextual AI is our RAG platform. We upload the scraped pages into a datastore, create a research agent, and then query it. The key differentiator: every answer comes with attributions — it tells you exactly which document and which section the answer came from."

> "Without Contextual AI, we'd need to set up embeddings, a vector database, retrieval logic, and a generation pipeline. Contextual gives us production-grade RAG in three API calls."

**OpenClaw + MCP — The interface:**

> "We packaged everything as an OpenClaw skill using the Model Context Protocol. OpenClaw discovers our four tools automatically, and the agent knows when and how to use them based on our SKILL.md instructions."

---

## 3. Live Demo + Code (~5 min)

### Demo Part 1: Show it working (~3 min)

**Open OpenClaw TUI (or Streamlit app as backup):**

```bash
openclaw tui
```

**Say:**

> "Let's scrape the Contextual AI documentation and ask it some questions."

**Type:**

```
Scrape https://docs.contextual.ai and tell me what Contextual AI does
```

**While it's running, narrate:**

> "Right now, Apify is spinning up a crawler in the cloud. It's visiting docs.contextual.ai, following links, and extracting text from each page. Then we upload all of that into a Contextual AI datastore and create a research agent."

**When the answer comes back:**

> "Notice the citations — every claim is attributed back to a specific source page. This isn't the model making things up. It's grounded in the actual documentation we just scraped."

**Ask a follow-up:**

```
How do I create an agent using their Python SDK?
```

> "Same conversation, same knowledge base. The agent remembers the context and answers from the same scraped material."

### Demo Part 2: Show the code (~2 min)

**Open `skills/web-researcher/server.py`:**

> "The entire skill is one Python file — about 150 lines. It's an MCP server that exposes four tools."

**Highlight `web_research_scrape`:**

> "This is the scraping tool. Five lines of Apify integration — we call their Website Content Crawler actor, wait for it to finish, and save the results as text files."

**Highlight `web_research_index`:**

> "This creates a Contextual AI datastore, creates a research agent, and uploads all the scraped documents. Three API calls."

**Highlight `web_research_query`:**

> "This is where the magic happens. We send the user's question to the Contextual AI agent, and it returns a grounded answer with attributions."

**Open `skills/web-researcher/SKILL.md`:**

> "And this is how OpenClaw knows what to do. The SKILL.md is essentially a prompt — it tells the agent what tools are available and what workflow to follow. Scrape first, then index, then query."

### Close (~30 sec)

> "In summary: Apify gave us live web data. Contextual AI gave us grounded, cited answers. OpenClaw gave us a natural language interface. The result is a skill that turns any website into a knowledge base in under a minute."

> "You could use this for onboarding onto a new API, researching a competitor's docs, or building a support bot grounded in your own documentation. And it's available on ClawHub for anyone to install."

---

## Backup Plan

If OpenClaw TUI has issues, use the Streamlit app:

```bash
uv run python main.py
```

If Apify is slow, have a pre-scraped demo ready — the agent we already created (agent ID: `03c2baf0-c6dc-4aff-a03c-f9dad14837d7`) has docs.contextual.ai indexed and can be queried immediately.

---

## Key Talking Points If Judges Ask Questions

**"Why not just use ChatGPT with web browsing?"**
> ChatGPT's browsing is slow, unreliable, and doesn't give you citations back to exact pages. We scrape the full site upfront and get structured, attributed answers.

**"How long does the scraping take?"**
> About 15-30 seconds for 5 pages. Apify runs the crawler in the cloud, so it's fast and doesn't depend on your local machine.

**"What happens with large sites?"**
> You set a page limit (up to 50). For really large sites, you'd want to scope it to a specific section. The Contextual AI datastore handles the rest.

**"Could this work with private/authenticated sites?"**
> Not yet with the current Apify crawler, but Apify supports authenticated scraping — that would be the next feature to add.

**"What's the path to production?"**
> Publish to ClawHub so any OpenClaw user can install it. Add caching so you don't re-scrape the same site. Add support for scheduled re-scraping to keep knowledge bases fresh.
