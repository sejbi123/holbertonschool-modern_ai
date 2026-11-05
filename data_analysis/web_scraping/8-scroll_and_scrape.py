#!/usr/bin/env python3
"""Scrape products from an infinite-scroll page."""

from bs4 import BeautifulSoup
fetch_html = __import__('0-fetch_html').fetch_html


def scroll_and_scrape(url, scroll_pause=2.0):
    """Return all unique products from the page."""
    html = fetch_html(url)
    soup = BeautifulSoup(html, 'html.parser')

    products = []
    seen = set()

    for card in soup.select('div.thumbnail'):
        title_tag = card.select_one('a.title')
        price_tag = card.select_one('h4.price')
        description_tag = card.select_one('p.description')

        if not title_tag or not price_tag or not description_tag:
            continue

        title = title_tag.get('title')
        price = price_tag.get_text(strip=True)
        description = description_tag.get_text(strip=True)

        rating = len(card.select('.ratings span.ws-icon-star'))

        key = (title, price)

        if key not in seen:
            seen.add(key)

            products.append({
                'title': title,
                'price': price,
                'description': description,
                'rating': rating
            })

    return products
