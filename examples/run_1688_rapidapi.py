#!/usr/bin/env python3
"""
1688 Wholesale & Factory Data — Real-Time Synchronous REST API Quickstart (RapidAPI Hub)
RapidAPI Hub: https://rapidapi.com/unitbytes/api/1688-wholesale-factory-data1
Docs & Schema: https://unitbytes.com/actors/1688-scraper/

Usage:
    pip install requests
    export RAPIDAPI_KEY="your_rapidapi_key"
    python examples/run_1688_rapidapi.py
"""

import os
import requests

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY", "YOUR_RAPIDAPI_KEY")
BASE_URL = "https://1688-wholesale-factory-data1.p.rapidapi.com"
HEADERS = {
    "x-rapidapi-host": "1688-wholesale-factory-data1.p.rapidapi.com",
    "x-rapidapi-key": RAPIDAPI_KEY,
}

# 1. Search verified 1688 Super Factories (GET /v1/1688/search)
search_res = requests.get(
    f"{BASE_URL}/v1/1688/search",
    headers=HEADERS,
    params={
        "keyword": "蓝牙耳机",
        "super_factory": "true",
        "sort_by": "sales",
        "page": 1,
        "page_size": 5,
    },
    timeout=30,
).json()

offers = search_res.get("data", {}).get("items", [])
print(f"Found {len(offers)} wholesale offers on page 1:")
for item in offers[:3]:
    print(f" - [{item.get('offerId')}] {item.get('title')} | ¥{item.get('price')} CNY")

# 2. Calculate Wholesale Order Cost & SKU Matrix (GET /v1/1688/product/skus)
offer_id = offers[0]["offerId"] if offers else "743829104821"
sku_res = requests.get(
    f"{BASE_URL}/v1/1688/product/skus",
    headers=HEADERS,
    params={"offer_id": offer_id, "order_quantity": 100},
    timeout=30,
).json().get("data", {})

print(
    f"\nOffer {offer_id} @ 100 units: "
    f"Unit Price = ¥{sku_res.get('matchedTierUnitPrice')} CNY | "
    f"Subtotal = ¥{sku_res.get('estimatedOrderTotalCny')} CNY | "
    f"SKUs = {sku_res.get('skuCount')}"
)

# 3. Calculate Amazon FBA Packaging Weight & CBM Volume (GET /v1/1688/product/logistics)
log_res = requests.get(
    f"{BASE_URL}/v1/1688/product/logistics",
    headers=HEADERS,
    params={"offer_id": offer_id, "order_quantity": 100},
    timeout=30,
).json().get("data", {})

print(
    f"Logistics (100 units): "
    f"Gross Weight = {log_res.get('totalGrossWeightKg')} kg | "
    f"Sea Volume = {log_res.get('totalVolumeCbm')} CBM | "
    f"Air Volumetric = {log_res.get('airVolumetricWeightKg')} kg"
)
