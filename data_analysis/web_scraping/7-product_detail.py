#!/usr/bin/env python3
"""Scrape details of a single product using Selenium."""

import time
from selenium import webdriver


def scrape_product_detail(url, delay=2.0):
    """Return the title, price, description, and rating of a product."""
    driver = webdriver.Chrome()

    try:
        driver.get(url)
        time.sleep(delay)

        title = driver.execute_script("""
            const headings = document.querySelectorAll('.caption h4');
            return headings.length > 1 ? headings[1].innerText.trim() : '';
        """)

        price = driver.execute_script("""
            const element = document.querySelector('h4.price');
            return element ? element.innerText.trim() : '';
        """)

        description = driver.execute_script("""
            const element = document.querySelector('p.description');
            return element ? element.innerText.trim() : '';
        """)

        rating = driver.execute_script("""
            return document.querySelectorAll(
                '.ratings p[data-rating]'
            ).length
                ? parseInt(document.querySelector(
                    '.ratings p[data-rating]'
                ).getAttribute('data-rating'))
                : document.querySelectorAll(
                    '.ratings .ws-icon-star'
                ).length;
        """)

        return {
            "title": title,
            "price": price,
            "description": description,
            "rating": rating
        }

    finally:
        driver.quit()
        