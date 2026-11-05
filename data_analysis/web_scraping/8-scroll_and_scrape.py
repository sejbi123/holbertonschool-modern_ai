#!/usr/bin/env python3
"""Scrape products from an infinite-scroll page."""

import time
from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=2.0):
    """Scroll the page and return all unique products."""
    """Configure Chrome in headless mode."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)

        """Count products before scrolling."""
        last_count = len(driver.find_elements(
            "css selector", "div.thumbnail"
        ))

        """Scroll until no new products appear."""
        while True:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

            """Wait for new products to load."""
            deadline = time.time() + scroll_pause
            new_count = last_count

            while new_count == last_count and time.time() < deadline:
                time.sleep(0.05)
                new_count = len(driver.find_elements(
                    "css selector", "div.thumbnail"
                ))

            if new_count == last_count:
                break

            last_count = new_count

        """Collect all product cards."""
        cards = driver.find_elements(
            "css selector", "div.thumbnail"
        )

        products = []
        seen = set()

        for card in cards:
            title = card.find_element(
                "css selector", "a.title"
            ).get_attribute("title")

            price = card.find_element(
                "css selector", "h4.price"
            ).text

            description = card.find_element(
                "css selector", "p.description"
            ).text

            rating = len(card.find_elements(
                "css selector",
                ".ratings span.ws-icon-star"
            ))

            """Avoid duplicate products."""
            key = (title, price)

            if key not in seen:
                seen.add(key)

                products.append({
                    "title": title,
                    "price": price,
                    "description": description,
                    "rating": rating
                })

        return products

    finally:
        """Close the browser."""
        driver.quit()
    