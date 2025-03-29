import os
from typing import List, Union, Optional, Dict

from dotenv import load_dotenv
from flask import flash
import requests


load_dotenv()

PROD_URL = os.getenv("PRODUCT_URL")


def get_products(url: str = PROD_URL) -> list:
    return requests.get(url).json()


def get_product(product_id: str, url: str = PROD_URL) -> Dict:
    return requests.get(url + product_id).json()


def add_product(name: str, description: str, price: float, img_url: str, url: str = PROD_URL):
    body = dict(
        name=name,
        description=description,
        price=price,
        img_url=img_url
    )

    msg = requests.post(url, json=body)
    flash(msg)


def update_product(product_id: str, name: str, description: str, price: float, img_url: str, url: str = PROD_URL):
    body = dict(
        name=name,
        description=description,
        price=price,
        img_url=img_url
    )
    msg = requests.put(url + product_id, json=body)
    flash(msg)