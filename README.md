# Web Researcher — OpenClaw Skill

> We built **Web Researcher** for **developers and researchers** so they can **scrape any website and ask grounded, cited questions about its content**, and we used **Apify** and **Contextual AI** to make **live web ingestion and hallucination-free answers** possible.

Built at [The Agent Toolkit — OpenClaw Hack Day](https://hackersquad.com) on March 25, 2026.

---

## The Problem

Developers and researchers waste time manually reading through documentation sites, knowledge bases, and blog posts to find specific answers. Copy-pasting content into ChatGPT loses citations and context. There's no quick way to turn a live website into a reliable, queryable knowledge base.

## The Solution

Web Researcher is an OpenClaw skill that:

1. **Scrapes** any website using Apify's Website Content Crawler
2. **Indexes** the scraped content into a Contextual AI datastore
3. **Answers** your questions with grounded, cited responses — no hallucinations

Ask OpenClaw: *"Scrape https://docs.example.com and tell me how their API auth works"* — and get an answer backed by real content with source citations.

## How It Works

```
User asks a question about a website
         │
         ▼
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────────┐
│   Apify          │     │  Contextual AI    │     │  OpenClaw Agent     │
│   Web Crawler    │────▶│  Datastore +      │────▶│  Grounded answer    │
│   (scrape site)  │     │  RAG Agent        │     │  with citations     │
└─────────────────┘     └──────────────────┘     └─────────────────────┘
```

### Tools Exposed to OpenClaw

| Tool | Description |
|------|-------------|
| `web_research_scrape` | Crawl a URL with Apify. Extracts text from up to 50 pages. |
| `web_research_index` | Upload scraped content to Contextual AI and create a research agent. |
| `web_research_query` | Ask a question. Returns a grounded answer with source attributions. |
| `web_research_status` | Check session state: what's scraped, indexed, and active. |

### Sponsor Tool Integration

- **Apify** pulls live web data — without it, we'd have no real content to work with. The Website Content Crawler handles JavaScript rendering, pagination, and structured text extraction across entire sites.
- **Contextual AI** grounds the agent's answers in the actual scraped material. Every answer comes with attributions back to source documents. This eliminates hallucinations — if the answer isn't in the docs, the agent says so.

## Setup

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager
- [OpenClaw CLI](https://docs.openclaw.ai/install) (`brew install openclaw-cli`)
- API keys for [Apify](https://console.apify.com) and [Contextual AI](https://app.contextual.ai)

### 1. Clone and install

```bash
git clone https://github.com/SankarSubbayya/agent-toolkit.git
cd agent-toolkit
uv sync
```

### 2. Set up environment variables

Create a `.env` file in the project root:

```bash
APIFY_API_TOKEN=your_apify_token_here
CONTEXTUAL_API_KEY=your_contextual_ai_key_here
```

### 3. Install the OpenClaw skill

```bash
mkdir -p ~/.openclaw/skills
cp -r skills/web-researcher ~/.openclaw/skills/web-researcher
```

Add the skill config to `~/.openclaw/openclaw.json` (merge into existing config):

```json
{
  "skills": {
    "entries": {
      "web-researcher": {
        "enabled": true,
        "env": {
          "APIFY_API_TOKEN": "your_apify_token_here",
          "CONTEXTUAL_API_KEY": "your_contextual_ai_key_here"
        }
      }
    }
  }
}
```

### 4. Verify the skill is loaded

```bash
openclaw skills list
```

You should see:

```
✓ ready   │ 🔬 web-researcher     │ openclaw-managed
```

### 5. Use it

```bash
openclaw tui
```

Then ask:

```
Scrape https://docs.contextual.ai and tell me what Contextual AI does
```

## Project Structure

```
agent-toolkit/
├── skills/
│   └── web-researcher/
│       ├── SKILL.md          # OpenClaw skill definition + instructions
│       └── server.py         # MCP server exposing 4 tools
├── agent.py                  # Contextual AI agent wrapper (standalone use)
├── scraper.py                # Apify scraper wrapper (standalone use)
├── app.py                    # Streamlit UI (alternative to OpenClaw)
├── main.py                   # Entry point for Streamlit app
├── openclaw.json             # MCP server config for OpenClaw
├── pyproject.toml            # Python dependencies
└── .env                      # API keys (not committed)
```

## Alternative: Streamlit UI

If you prefer a web UI instead of OpenClaw:

```bash
uv run python main.py
```

This launches a Streamlit app with a sidebar for scraping and a chat interface for Q&A.

## Demo

### What we built

An OpenClaw skill called Web Researcher that scrapes websites and lets you chat with the content using grounded, cited answers.

### What problem we're solving

Developers waste time manually reading through scattered docs and knowledge bases. Pasting content into an LLM loses citations and introduces hallucinations.

### How we used the tools

- **Apify** pulls the live source data — crawls websites, extracts clean text, handles pagination
- **Contextual AI** grounds the agent on the scraped material — every answer includes source attributions

### What the tools enabled us to do

- **Using Apify** let us work with live web data instead of fake sample data — any URL becomes a knowledge base in minutes
- **Using Contextual AI** let the agent answer from real technical material instead of hallucinating — with citations back to exact source pages

## Team

- **Sankaranarayanan Subbayya** — [sankara68@gmail.com](mailto:sankara68@gmail.com)

## Tech Stack

- Python 3.12
- [Apify](https://apify.com) — Web scraping and content extraction
- [Contextual AI](https://contextual.ai) — RAG platform with grounded answers
- [OpenClaw](https://docs.openclaw.ai) — AI agent framework
- [MCP](https://modelcontextprotocol.io) — Model Context Protocol for tool integration
- [Streamlit](https://streamlit.io) — Alternative web UI

## License

MIT
