#!/usr/bin/env python3
"""Scrape details of a single product using Selenium."""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def scrape_product_detail(url, delay=2.0):
    """Return the details of a single product."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(delay)

        caption = driver.find_element(By.CSS_SELECTOR, ".caption")
        title = caption.find_elements(By.TAG_NAME, "h4")[1].text

        price = driver.find_element(
            By.CSS_SELECTOR, "h4.price"
        ).text

        description = driver.find_element(
            By.CSS_SELECTOR, "p.description"
        ).text

        ratings = driver.find_elements(
            By.CSS_SELECTOR, ".ratings p.ws-icon.ws-icon-star"
        )
        rating = len(ratings)

        return {
            "title": title,
            "price": price,
            "description": description,
            "rating": rating
        }

    finally:
        driver.quit()
