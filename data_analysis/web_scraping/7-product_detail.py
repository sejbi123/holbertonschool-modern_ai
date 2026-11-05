#!/usr/bin/env python3
"""Scrape the details of a single product page."""

import time
from selenium import webdriver


def scrape_product_detail(url, delay=2.0):
    """Return the details of the product page at `url`."""
    
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)

        # give the page time to render before reading it
        time.sleep(delay)

        # the rating is the count of star icons, so find_elements is used
        return {
                "title": driver.find_element(
                    "css selector", ".caption h4.title"
                    ).text,
                "price": driver.find_element(
                    "css selector", ".caption h4.price"
                    ).text,
                "description": driver.find_element(
                    "css selector", ".caption p.description"
                    ).text,
                "rating": len(
                    driver.find_elements(
                        "css selector", ".ratings .ws-icon-star"
                        )
                    ),
            }

    finally:
        driver.quit()
    