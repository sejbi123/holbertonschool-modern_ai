#!/usr/bin/env python3
"""Log in to Quotes to Scrape and extract quotes."""

import requests
from bs4 import BeautifulSoup


def login_and_scrape(login_url, user, pwd):
    """Log in and return quotes visible after authentication."""
    session = requests.Session()

    response = session.get(login_url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    csrf_input = soup.find("input", {"name": "csrf_token"})
    if csrf_input is None:
        raise ValueError("CSRF token not found")

    csrf_token = csrf_input.get("value")

    login_data = {
        "username": user,
        "password": pwd,
        "csrf_token": csrf_token
    }

    response = session.post(
        login_url,
        data=login_data,
        timeout=10
    )
    response.raise_for_status()

    quotes_url = "https://quotes.toscrape.com/"
    response = session.get(quotes_url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = []

    for quote in soup.find_all("div", class_="quote"):
        text_element = quote.find("span", class_="text")
        author_element = quote.find("small", class_="author")
        tag_elements = quote.find_all("a", class_="tag")

        if text_element is None or author_element is None:
            continue

        quotes.append({
            "text": text_element.get_text(strip=True),
            "author": author_element.get_text(strip=True),
            "tags": [
                tag.get_text(strip=True) for tag in tag_elements
            ]
        })

    return quotes
