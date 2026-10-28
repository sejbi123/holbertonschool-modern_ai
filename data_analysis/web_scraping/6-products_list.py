#!/usr/bin/env python3
"""Scrape products from a static category page."""

import time
from selenium import webdriver


def scrape_products(url):
    """Extract product details from a category page."""
    driver = webdriver.Chrome()
    products = []

    try:
        driver.get(url)
        time.sleep(2)

        product_elements = driver.execute_script("""
            return Array.from(
                document.querySelectorAll('.thumbnail')
            ).map(product => {
                const title = product.querySelector('a.title');
                const price = product.querySelector('h4.price');
                const description = product.querySelector('p.description');
                const rating = product.querySelector(
                    '.ratings p[data-rating]'
                );

                return {
                    title: title ? title.getAttribute('title') : '',
                    price: price ? price.innerText.trim() : '',
                    description: description
                        ? description.innerText.trim() : '',
                    rating: rating
                        ? parseInt(rating.getAttribute('data-rating'))
                        : 0
                };
            });
        """)

        for product in product_elements:
            products.append(product)

    finally:
        driver.quit()

    return products
