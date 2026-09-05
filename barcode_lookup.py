#barcode_lookup.py

import requests
from currency import *

import os

API_KEY = os.getenv("BARCODE_LOOKUP_API_KEY")


def lookup(barcode: int) ->str:
    '''Uses Barcode Lookup API to find books matching the ISBN number online'''
    
    url = f'https://api.barcodelookup.com/v3/products?barcode={barcode}&formatted=y&key={API_KEY}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
    else:
        data = None
        print("Error:", response.status_code)

    if not data:
        print("Product not found")
        return

    if 'products' not in data or len(data['products']) == 0:
           print("Product not found")
           return

    product = data["products"][0]
    return product["stores"]


