#!/usr/bin/env python3
"""Scrape products from a static category page."""

import time
from selenium import webdriver


def scrape_products_list(url):
    """Extract product details from a category page."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    products = []

    try:
        driver.get(url)
        time.sleep(2)

        product_elements = driver.find_elements(
            "css selector", ".thumbnail"
        )

        for product in product_elements:
            title_element = product.find_element(
                "css selector", "a.title"
            )
            price_element = product.find_element(
                "css selector", "h4.price"
            )
            description_element = product.find_element(
                "css selector", "p.description"
            )
            rating_element = product.find_element(
                "css selector", ".ratings p[data-rating]"
            )

            products.append({
                "title": title_element.get_attribute("title"),
                "price": price_element.text,
                "description": description_element.text,
                "rating": int(
                    rating_element.get_attribute("data-rating")
                )
            })

    finally:
        driver.quit()

    return products
