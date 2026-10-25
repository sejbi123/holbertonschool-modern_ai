#!/usr/bin/env python3
"""Scrape quotes using the site's API."""

import json

fetch_html = __import__('0-fetch_html').fetch_html


def scrape_via_api(base_url):
    """Fetch quotes from all API pages."""
    quotes = []
    page = 1

    while True:
        url = f"{base_url}/api/quotes?page={page}"
        response = fetch_html(url)
        data = json.loads(response)

        page_quotes = data.get("quotes", [])

        if not page_quotes:
            break

        for quote in page_quotes:
            quotes.append({
                "text": quote["text"],
                "author": quote["author"]["name"],
                "tags": quote["tags"]
            })

        page += 1

    return quotes
