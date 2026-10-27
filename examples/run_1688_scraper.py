#!/usr/bin/env python3
"""
1688 Scraper & Price Monitor: Wholesale & Product API — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/1688-scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/1688-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/1688-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_1688_scraper.py
"""

import os
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "queries": ["phone case"],
    "maxItems": 30,
    "detailLevel": "full",
    "sortBy": "normal",
    "verticalProductFlag": "factory"
}

run = client.actor("unitbytes/1688-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("price"), item.get("priceDisplay"))
