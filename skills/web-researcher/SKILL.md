---
name: web-researcher
description: Scrape any website with Apify and ask grounded questions about its content using Contextual AI. Turns live web pages into a knowledge base you can chat with.
version: 1.0.0
metadata:
  openclaw:
    requires:
      env:
        - APIFY_API_TOKEN
        - CONTEXTUAL_API_KEY
      bins:
        - python3
    primaryEnv: CONTEXTUAL_API_KEY
    emoji: "🔬"
---

# Web Researcher

A research skill that scrapes websites using Apify and lets you ask grounded, cited questions about the content using Contextual AI.

## Purpose

Developers and researchers waste time manually reading through documentation sites, blog posts, and knowledge bases. This skill automates the process: scrape a site, index it, and ask questions — with cited answers grounded in real content, not hallucinations.

## Available Tools

- `web_research_scrape` — Scrape a URL using Apify's Website Content Crawler. Returns structured page content. Accepts a URL and optional max_pages (default 5).
- `web_research_index` — Upload scraped content to a Contextual AI datastore and create a research agent. Call this after scraping.
- `web_research_query` — Ask a question about the scraped and indexed content. Returns a grounded answer with source citations.
- `web_research_status` — Check the current state: what has been scraped, whether an agent is active, and how many documents are indexed.

## Workflow

1. The user provides a URL to research.
2. Call `web_research_scrape` with the URL. This uses Apify to crawl the site and extract text content.
3. Call `web_research_index` to upload the scraped pages to Contextual AI and create a research agent.
4. The user asks questions. Call `web_research_query` for each question. The agent returns answers grounded in the scraped content with source attributions.

## Rules

- Always scrape before indexing. Always index before querying.
- If the user provides a new URL, scrape and index it before answering questions about it.
- When presenting answers, always include the source citations from attributions.
- If the query returns no relevant results, say so clearly rather than guessing.
- Do NOT call `web_research_query` without first completing scrape and index steps.
- Default to 5 pages unless the user specifies otherwise. Maximum 50 pages.
