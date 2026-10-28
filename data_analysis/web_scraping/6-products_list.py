#!/usr/bin/env python3
"""Scrape products from a static category page."""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def scrape_products(url):
    """Extract product details from a category page."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    products = []

    try:
        driver.get(url)
        time.sleep(2)

         product_elements = driver.find_elements(
            By.CSS_SELECTOR, ".thumbnail"
        )

        for product in product_elements:
            title_element = product.find_element(
                By.CSS_SELECTOR, "a.title"
            )
            price_element = product.find_element(
                By.CSS_SELECTOR, "h4.price"
            )
            description_element = product.find_element(
                By.CSS_SELECTOR, "p.description"
            )
            rating_element = product.find_element(
                By.CSS_SELECTOR, ".ratings p[data-rating]"
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
