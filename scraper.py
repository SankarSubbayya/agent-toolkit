import os
import tempfile
from apify_client import ApifyClient


def scrape_url(url: str, max_pages: int = 10) -> list[dict]:
    """Scrape a URL using Apify's Website Content Crawler and return page results."""
    client = ApifyClient(os.environ["APIFY_API_TOKEN"])

    run_input = {
        "startUrls": [{"url": url}],
        "maxCrawlPages": max_pages,
        "crawlerType": "cheerio",
    }

    run = client.actor("apify/website-content-crawler").call(run_input=run_input)
    items = list(client.dataset(run["defaultDatasetId"]).iterate_items())
    return items


def save_scraped_pages(items: list[dict], output_dir: str | None = None) -> list[str]:
    """Save scraped page content as text files. Returns list of file paths."""
    if output_dir is None:
        output_dir = tempfile.mkdtemp(prefix="agent_toolkit_")

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

    return paths
