#!/usr/bin/env python3
"""
1688 Scraper: Fastest 1688.com Wholesale & Factory Finder 🇨🇳 — Official Python Quickstart
Actor: https://apify.com/unitbytes/1688-scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/1688-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/1688-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_1688_scraper.py
"""

import json
import os
from apify_client import ApifyClient

# Read API token from environment (or paste your token directly for local testing)
APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")


def main():
    client = ApifyClient(APIFY_API_TOKEN)
    
    
    run_input = {
        "queries": ["phone case"],
        "maxItems": 30,
        "detailLevel": "full",
        "proxyConfiguration": {
            "useApifyProxy": True
        }
    }
    
    run = client.actor("unitbytes/1688-scraper").call(run_input=run_input)
    
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        print(item.get("title"), item.get("price"), item.get("priceDisplay"))


if __name__ == "__main__":
    main()
