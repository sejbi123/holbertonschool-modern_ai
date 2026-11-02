#!/usr/bin/env python3
"""Module that scrapes products from an infinite-scroll page."""
import time
from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=2.0):
    """Scroll an infinite-scroll page and scrape all unique products."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        last_height = driver.execute_script(
            "return document.body.scrollHeight")
        while True:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause)
            new_height = driver.execute_script(
                "return document.body.scrollHeight")
            if new_height <= last_height:
                break
            last_height = new_height

        products = []
        seen = set()
        for card in driver.find_elements("css selector", "div.thumbnail"):
            title = card.find_element(
                "css selector", "a.title").get_attribute("title")
            price = card.find_element("css selector", "h4.price").text
            if (title, price) in seen:
                continue
            seen.add((title, price))
            description = card.find_element(
                "css selector", "p.description").text
            rating = len(card.find_elements(
                "css selector", ".ratings p.ws-icon.ws-icon-star"))
            products.append({
                "title": title,
                "price": price,
                "description": description,
                "rating": rating
            })
        return products
    finally:
        driver.quit()
