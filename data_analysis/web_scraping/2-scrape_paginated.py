#!/usr/bin/env python3
"""Scrape quotes from multiple pages."""

from bs4 import BeautifulSoup
import time
from urllib import parse

fetch_html = __import__('0-fetch_html').fetch_html
scrape_basic = __import__('1-scrape_basic').scrape_basic


def scrape_paginated(base_url):
    """Scrape quotes from all available pages."""
    all_quotes = []
    url = base_url

    while url:
        html = fetch_html(url)
        soup = BeautifulSoup(html, 'html.parser')

        all_quotes.extend(scrape_basic(url))

        next_link = soup.select_one('li.next a')

        if next_link:
            url = parse.urljoin(url, next_link['href'])
            time.sleep(1)
        else:
            break

    return all_quotes
