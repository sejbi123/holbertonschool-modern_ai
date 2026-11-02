#!/usr/bin/env python3
"""Module that scrapes the details of a single product page."""
import time
from selenium import webdriver


def scrape_product_detail(url, delay=2.0):
    """Open a product detail page and return its details."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        time.sleep(delay)
        title = driver.find_elements(
            "css selector", ".caption h4")[1].text
        price = driver.find_element(
            "css selector", "h4.price").text
        description = driver.find_element(
            "css selector", "p.description").text
        rating = len(driver.find_elements(
            "css selector", ".ratings p.ws-icon.ws-icon-star"))
        return {
            "title": title,
            "price": price,
            "description": description,
            "rating": rating
        }
    finally:
        driver.quit()
    