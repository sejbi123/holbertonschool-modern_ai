#!/usr/bin/env python3
"""Extract quotes from JSON-LD embedded in a web page."""

import json
from bs4 import BeautifulSoup

fetch_html = __import__('0-fetch_html').fetch_html


def extract_jsonld(url):
    """Extract quote data from JSON-LD scripts."""
    html = fetch_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    quotes = []

    scripts = soup.find_all(
        'script',
        type='application/ld+json'
    )

    for script in scripts:
        try:
            data = json.loads(script.string or script.get_text())
        except (json.JSONDecodeError, TypeError):
            continue

        objects = data if isinstance(data, list) else [data]

        for obj in objects:
            if not isinstance(obj, dict):
                continue

            if obj.get("@type") != "Quote":
                continue

            tags = obj.get("keywords", [])

            if isinstance(tags, str):
                tags = [tag.strip() for tag in tags.split(",")]

            quotes.append({
                "text": obj.get("text"),
                "author": obj.get("author", {}).get("name")
                if isinstance(obj.get("author"), dict)
                else None,
                "tags": tags
            })

    return quotes
