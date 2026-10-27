# 🇨🇳 1688.com Wholesale, Factory & Reverse Image Search Scraper + REST API Suite (`$1.50 / 1K`)

<div align="center">

[![Available on Apify](https://img.shields.io/badge/Available_on-Apify-28B52A?style=for-the-badge&logo=apify&logoColor=white)](https://apify.com/unitbytes/1688-scraper?fpr=939u3w&fp_sid=gh_1688)
[![n8n Creator Hub](https://img.shields.io/badge/n8n_Creator_Hub-@unitbytes-EA4B71?style=for-the-badge&logo=n8n&logoColor=white)](https://n8n.io/creators/unitbytes/)
[![Zero Login](https://img.shields.io/badge/Account_Required-None-blue?style=for-the-badge)](https://apify.com/unitbytes/1688-scraper?fpr=939u3w&fp_sid=gh_1688)
[![Pricing](https://img.shields.io/badge/Pricing-Pay_Per_Result-orange?style=for-the-badge)](https://apify.com/unitbytes/1688-scraper?fpr=939u3w&fp_sid=gh_1688)

**The fastest zero-login 1688.com (阿里巴巴) China B2B wholesale & factory data extraction suite on Apify (`$1.50 / 1,000 items`) and synchronous REST API (`<500ms` GET on RapidAPI Hub, Zyla API Hub & Apify Standby). Extract Verified Super Factories (超级工厂), tiered CNY volume pricing, MOQ, SKU matrices, Amazon FBA packaging specs (weight/CBM), and photo-to-factory visual search.**

[**🚀 Try Live on Apify**](https://apify.com/unitbytes/1688-scraper?fpr=939u3w&fp_sid=gh_1688) • [**⚡ Official n8n Creator Hub**](https://n8n.io/creators/unitbytes/) • [**🔧 39 Free n8n Templates**](https://unitbytes.com/n8n/) • [**📖 Documentation & Schemas**](https://unitbytes.com/actors/) • [**📚 Engineering Playbooks**](https://unitbytes.com/blog/)

</div>

---

<p align="center">
  <a href="https://apify.com/unitbytes/1688-scraper?fpr=939u3w&fp_sid=gh_1688" target="_blank">
    <img src="https://raw.githubusercontent.com/unitbytes/.github/main/assets/banners/unitbytes-1688-wholesale-factory-supplier-scraper-banner.jpg" alt="🇨🇳 1688.com Wholesale, Factory & Reverse Image Search Scraper + REST API Suite (`$1.50 / 1K`)" width="100%" />
  </a>
</p>

<p align="center">
  <a href="https://apify.com/unitbytes/1688-scraper?fpr=939u3w&fp_sid=gh_1688" target="_blank">
    <img src="https://raw.githubusercontent.com/unitbytes/.github/main/assets/try-it-for-free.svg" width="240" height="48" alt="Try it for Free">
  </a>
  <br>
  <sub>⚡ <b>1-Click Free Trial:</b> Test live queries using Apify's `$5` free monthly credit • Zero login or cookies required</sub>
</p>

---

<!-- UNITBYTES_REPO_KIT_START -->
## 📦 Included in This Repository (Python Quickstarts, n8n Workflows, MCP & Sample Data)

This repository contains ready-to-run **Python SDK scripts**, **9-node n8n automation workflow `.json` templates**, **AI Agent MCP configuration (`.cursor/mcp.json`)**, and **sample output datasets (JSON & CSV)**:

| Extraction Engine | 🐍 Python SDK Quickstart | ⚡ n8n Workflow Template | 📊 Sample Output | 🚀 Cloud Console |
| :--- | :--- | :--- | :---: | :---: |
| **1688 Scraper & Price Monitor: Wholesale & Product API**<br><sub>[`unitbytes/1688-scraper`](https://apify.com/unitbytes/1688-scraper?fpr=939u3w&fp_sid=gh_1688) • [Full Schema](https://unitbytes.com/actors/1688-scraper/) • [Engineering Playbook](https://unitbytes.com/blog/how-to-scrape-1688-without-account-sourcing-guide/)</sub> | [`examples/run_1688_scraper.py`](examples/run_1688_scraper.py) | [`n8n/1688-scraper-n8n-workflow.json`](n8n/1688-scraper-n8n-workflow.json)<br><sub>[⚡ Official on n8n.io ↗](https://n8n.io/workflows/21097-extract-1688com-product-data-to-csv-with-unitbytes-and-apify/)</sub> | [`JSON`](samples/1688-scraper-sample.json) · [`CSV`](samples/1688-scraper-sample.csv) | [⚡ **Run on Apify**](https://apify.com/unitbytes/1688-scraper?fpr=939u3w&fp_sid=gh_1688) |
| **1688 Image Search Scraper: Suppliers & Factories by Photo**<br><sub>[`unitbytes/1688-image-search-scraper`](https://apify.com/unitbytes/1688-image-search-scraper?fpr=939u3w&fp_sid=gh_1688) • [Full Schema](https://unitbytes.com/actors/1688-image-search-scraper/) • [Engineering Playbook](https://unitbytes.com/blog/1688-image-search-alibaba-b2b-supplier-api-sourcing-guide/)</sub> | [`examples/run_1688_image_search_scraper.py`](examples/run_1688_image_search_scraper.py) | [`n8n/1688-image-search-scraper-n8n-workflow.json`](n8n/1688-image-search-scraper-n8n-workflow.json)<br><sub>[⚡ Official on n8n.io ↗](https://n8n.io/workflows/21097-extract-1688com-product-data-to-csv-with-unitbytes-and-apify/)</sub> | [`JSON`](samples/1688-image-search-scraper-sample.json) · [`CSV`](samples/1688-image-search-scraper-sample.csv) | [⚡ **Run on Apify**](https://apify.com/unitbytes/1688-image-search-scraper?fpr=939u3w&fp_sid=gh_1688) |
| **1688 Wholesale & Factory Synchronous REST API (`<500ms` GET)**<br><sub>[RapidAPI Hub](https://rapidapi.com/unitbytes/api/1688-wholesale-factory-data1) • [Zyla API Hub](https://zylalabs.com/api-marketplace/commerce+%26+ecommerce/china+b2b+wholesale+and+factory+data+api/14468) • [Apify Standby](https://apify.com/unitbytes/1688-scraper?fpr=939u3w&fp_sid=gh_1688)</sub> | [`examples/run_1688_rapidapi.py`](examples/run_1688_rapidapi.py) | [`n8n/1688-scraper-n8n-workflow.json`](n8n/1688-scraper-n8n-workflow.json) | [`JSON`](samples/1688-scraper-sample.json) · [`CSV`](samples/1688-scraper-sample.csv) | [⚡ **RapidAPI**](https://rapidapi.com/unitbytes/api/1688-wholesale-factory-data1) · [⚡ **Zyla**](https://zylalabs.com/api-marketplace/commerce+%26+ecommerce/china+b2b+wholesale+and+factory+data+api/14468) |

- 🤖 **Cursor, Windsurf & Claude Code MCP Ready:** Includes [`.cursor/mcp.json`](.cursor/mcp.json) pre-configured with `https://mcp.apify.com` so AI coding agents can invoke these UnitBytes scrapers natively.
- 💡 **Using n8n?** Explore our official creator profile at **[n8n.io/creators/unitbytes](https://n8n.io/creators/unitbytes/)** or copy all 39 pre-built 9-node scraping workflows (`Ctrl+V`) at **[unitbytes.com/n8n](https://unitbytes.com/n8n/)**.
- 📚 **Engineering Playbooks:** [**APAC Sourcing Playbook**](https://unitbytes.com/blog/how-to-scrape-1688-without-account-sourcing-guide/) • [**Photo-to-Factory Sourcing Playbook**](https://unitbytes.com/blog/1688-image-search-alibaba-b2b-supplier-api-sourcing-guide/) — or browse all guides at **[unitbytes.com/blog](https://unitbytes.com/blog/)**.
<!-- UNITBYTES_REPO_KIT_END -->

---

## ⚡ Pre-Configured 1-Click Task Presets

Launch pre-configured extraction templates directly in the Apify Cloud Console with zero parameter setup:

| Task Preset | Target Extraction Use Case | Direct Launch |
| :--- | :--- | :---: |
| **1688 Phone Cases & Accessories Wholesale Sourcing** | Source phone cases and mobile accessories from top Guangdong factories with full variant matrices and wholesale pricing. | [⚡ Run Task Preset](https://apify.com/unitbytes/1688-scraper/examples/1688-phone-case-accessories-wholesale?fpr=939u3w&fp_sid=gh_1688) |
| **1688 TWS Wireless Earbuds & Audio Factory Sourcing** | Source TWS Bluetooth 5.3 wireless earbuds and audio equipment directly from certified Guangdong audio manufacturers with FBA package weights. | [⚡ Run Task Preset](https://apify.com/unitbytes/1688-scraper/examples/1688-wireless-earbuds-audio-manufacturers?fpr=939u3w&fp_sid=gh_1688) |
| **1688 Smart Watch & Wearable Tech Manufacturers** | Find top smartwatch, fitness band, and wearable electronics manufacturers directly from verified Super Factories in Shenzhen and Guangdong. | [⚡ Run Task Preset](https://apify.com/unitbytes/1688-scraper/examples/1688-smart-watch-electronics-procurement?fpr=939u3w&fp_sid=gh_1688) |
| **1688 Streetwear Hoodies & Apparel Manufacturers** | Source French terry blanks, heavyweight hoodies, and custom streetwear apparel directly from audited OEM clothing manufacturers. | [⚡ Run Task Preset](https://apify.com/unitbytes/1688-scraper/examples/1688-hoodies-streetwear-apparel-factory?fpr=939u3w&fp_sid=gh_1688) |
| **1688 Travel Backpacks & Luggage OEM Factories** | Find waterproof travel bags, school backpacks, and luggage manufacturers with tiered bulk discounts and OEM custom branding. | [⚡ Run Task Preset](https://apify.com/unitbytes/1688-scraper/examples/1688-backpacks-travel-luggage-wholesale?fpr=939u3w&fp_sid=gh_1688) |
| **1688 Home & Kitchen Gadgets Manufacturer Direct** | Source silicone kitchen gadgets, food storage organizers, and trending home products directly from certified Chinese houseware factories. | [⚡ Run Task Preset](https://apify.com/unitbytes/1688-scraper/examples/1688-home-kitchen-gadgets-manufacturer?fpr=939u3w&fp_sid=gh_1688) |
| **Reverse Image Search 1688.com Source Factories from Product Photos** | Upload or pass any Amazon, Shopify, or TikTok Shop product image URL to find identical OEM manufacturers and RMB wholesale tiers on 1688.com. | [⚡ Run Task Preset](https://apify.com/unitbytes/1688-image-search-scraper?fpr=939u3w&fp_sid=gh_1688) |

---

## 🛠️ Extraction Engines in This Suite

### 🚀 1688 Scraper & Price Monitor: Wholesale & Product API (`unitbytes/1688-scraper`)

Ultra-fast 1688.com product scraper & price monitor API (from `$0.0015`). Extract real-time factory prices, MOQ, stock inventory, SKU variants, Amazon FBA packaging specs, and verified manufacturers with zero login. MCP & AI Agent ready.

- **Pricing:** `$0.0015 / item` (Pay-Per-Event — `$0.0015` search product listing, `$0.0025` full b2b product detail & spec matrix (volume tiers from `$0.0009`))
- **Cloud Console:** [https://apify.com/unitbytes/1688-scraper?fpr=939u3w&fp_sid=gh_1688](https://apify.com/unitbytes/1688-scraper?fpr=939u3w&fp_sid=gh_1688)
- **Full Documentation & Schema:** [https://unitbytes.com/actors/1688-scraper/](https://unitbytes.com/actors/1688-scraper/)
- **n8n Workflow File:** [`n8n/1688-scraper-n8n-workflow.json`](n8n/1688-scraper-n8n-workflow.json)
- **Engineering Playbook:** [How to Scrape 1688.com Without an Account in 2026 (The Importer's Sourcing Guide)](https://unitbytes.com/blog/how-to-scrape-1688-without-account-sourcing-guide/)

#### Key Capabilities
- **Tiered Volume Price Breaks:** Captures complete wholesale discount structures across 1-piece sample, carton, and factory pallet order tiers.
- **Supplier Trust & Factory Verification:** Extracts years in business, registered capital, factory location, and Alibaba China verified merchant badges.
- **Granular SKU Variation Matrix:** Extracts colorways, sizing tables, per-SKU inventory levels, and individual SKU price variants in structured JSON.
- **Resilient Anti-Bot Navigation:** Built-in anti-bot resilience and automatic session management for uninterrupted wholesale catalog extraction.

#### ⚙️ Input Parameters (Schema)

| Parameter | Type | Default / Prefill | Description |
| :--- | :---: | :--- | :--- |
| `queries` | `array` | `["phone case"]` | List of product keywords to search on 1688.com (e.g., ['phone case', 'smart watch', '蓝牙耳机']). Scrapes multiple keywords in a single run. |
| `keyword` | `string` | — | Single keyword in English or Chinese (e.g. 'phone case', '手机壳', '蓝牙耳机') or a numeric 1688 offer ID (e.g. '680000000001'). If provided, it is added to the search queries. Ignored if startUrls or offerIds are provided. |
| `offerIds` | `array` | — | Optional list of numeric 1688 wholesale product offer IDs (e.g. '680000000001', '1015804349214'). Directly extracts full B2B details, tiered volume prices, and SKU matrices for each product without searching. |
| `startUrls` | `array` | — | Paste any 1688 URLs directly from your browser: direct product offer links (e.g. 'https://detail.1688.com/offer/680000000001.html') or search listing URLs (e.g. 'https://s.1688.com/selloffer/offer_search.htm?keywords=hoodie'). You can also use 'Direct Offer IDs' to enter raw IDs. |
| `searchUrls` | `array` | — | Optional list of 1688 search listing URLs. Note: you can also paste search URLs directly into 'Start URLs' above. |
| `maxItems` | `integer` | `30` | Maximum number of wholesale offers to scrape (1 to 10,000). |
| `resumptionToken` | `string` | — | Optional encrypted resumption token copied from a previous run, Key-Value store, or dataset item. Restores the exact session and continues scraping directly from where it left off without starting over. |
| `detailLevel` | `string` | `full` | Choose 'Full B2B Mode' for complete wholesale tiered volume prices, full color/size SKU variations, MOQ, and verified factory audit badges, or 'Summary Mode' for fast product search card discovery. |
| `sortBy` | `string` | `normal` | Sorting order for listings. Note: To target products in a specific price bracket without losing search relevance, use 'Min Price' and 'Max Price' below. |
| `priceMin` | `integer` | — | Minimum unit wholesale price in Chinese Yuan (CNY ¥). Server-side filtered natively by 1688. |
| `priceMax` | `integer` | — | Maximum unit wholesale price in Chinese Yuan (CNY ¥). Server-side filtered natively by 1688. |
| `province` | `string` | — | Filter by Chinese manufacturing province (e.g. '广东' for Guangdong/Shenzhen/Guangzhou, '浙江' for Zhejiang/Yiwu/Hangzhou, '江苏' for Jiangsu). |
| `verticalProductFlag` | `string` | `factory` | Select the 1688 wholesale channel to query directly at source: 'Direct Factory' for OEM/ODM manufacturers, 'Super Factory' for top mega-factories, 'Cross-Border' for Amazon FBA/export sellers, 'Ready-to-Ship' for in-stock spot items, or 'All Channels'. |
| `proxyConfiguration` | `object` | `{"useApifyProxy": true}` | Apify Proxy configuration for fast worldwide access. Apify Residential proxy is recommended for high-volume extraction. |

#### ⚡ Real-Time Synchronous REST API (RapidAPI Hub, Zyla API Hub & Apify Standby — `<500ms` GET)

Need **instant synchronous `GET` JSON responses (`<500ms` live / `<150ms` cached)** for a live sourcing portal, ERP, or FBA landed-cost calculator without polling batch runs? Use our **1688 Wholesale & Factory Data Synchronous REST API**:

- 👉 **[Test Live on RapidAPI Hub (`$0` Free Tier)](https://rapidapi.com/unitbytes/api/1688-wholesale-factory-data1)** (`x-rapidapi-host: 1688-wholesale-factory-data1.p.rapidapi.com`)
- 👉 **[Test Live on Zyla API Hub](https://zylalabs.com/api-marketplace/commerce+%26+ecommerce/china+b2b+wholesale+and+factory+data+api/14468)** (Listing ID `14468`)
- ⚡ **[Apify Multi-Tenant Standby Server](https://apify.com/unitbytes/1688-scraper?fpr=939u3w&fp_sid=gh_1688)** (`https://unitbytes--1688-scraper.apify.actor` with `Authorization: Bearer <APIFY_TOKEN>`)
- 🐍 **Runnable Python Script:** [`examples/run_1688_rapidapi.py`](examples/run_1688_rapidapi.py)

| Category | Endpoint | Method | Description |
| :--- | :--- | :---: | :--- |
| **1. Factory & Wholesale Search** | `/v1/1688/search` (`/v1/search`) | `GET` | Search 1688.com wholesale catalog in CNY with `super_factory=true` (超级工厂), `sort_by=sales`, `min_price`, `max_price`, and server-side pagination. |
| **2. Visual Photo-to-Factory Search** | `/v1/image-search` | `GET`/`POST` | Upload or pass any Amazon/Shopify/AliExpress product image URL (`image_url`) to find the exact 1688 OEM factory and CNY tiered wholesale prices. |
| **3. Product & SKU Intelligence** | `/v1/1688/product` (`/v1/offer`) | `GET` | Complete 1688 offer detail: CNY ladder pricing (`tieredPrices`), MOQ, SKU matrix (`skuMatrix`), factory badges, and 3-axis merchant scores. |
| **3. Product & SKU Intelligence** | `/v1/1688/product/skus` | `GET` | Calculate active CNY unit tier price (`matchedTierUnitPrice`) and total order subtotal (`estimatedOrderTotalCny`) for a target `order_quantity`. |
| **3. Product & SKU Intelligence** | `/v1/offers/batch` | `GET` | Concurrent batch lookup for multiple 1688 `offer_ids` in a single request. |
| **4. FBA Logistics & Supplier Intel** | `/v1/1688/product/logistics` | `GET` | Extract unit weight (`kg`), carton dimensions (`cm`), shipping origin, and calculate total gross weight, sea volume (`CBM`), and air volumetric weight. |
| **4. FBA Logistics & Supplier Intel** | `/v1/1688/supplier` | `GET` | Extract factory storefront profile, business license verification, repeat buyer rate (`repeatBuyerRate`), and factory floor credentials. |

#### Python SDK Quickstart (`examples/run_1688_scraper.py`)
```python
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
```

#### Sample Output Schema (`samples/1688-scraper-sample.json`)
```json
{
  "id": "680000000001",
  "offerId": "680000000001",
  "url": "https://detail.1688.com/offer/680000000001.html",
  "title": "适用苹果x手机壳iPhoneX保护套iponex新款ipx液态硅胶ix外壳纯色",
  "page": 1,
  "position": 1,
  "nextPage": 2,
  "price": 1.8,
  "currency": "CNY",
  "priceDisplay": "1.40 - 1.80",
  "minOrderQuantity": 1,
  "totalStock": 43557,
  "salesVolume": "已售10万+件",
  "repurchaseRate": "38.5%",
  "superFactory": true,
  "factoryInspection": true,
  "tieredPrices": [
    {
      "minQuantity": 1,
      "maxQuantity": 499,
      "price": 1.8,
      "unit": "件"
    },
    {
      "minQuantity": 500,
      "maxQuantity": 999,
      "price": 1.6,
      "unit": "件"
    },
    {
      "minQuantity": 1000,
      "maxQuantity": null,
      "price": 1.4,
      "unit": "件"
    }
  ],
  "pictureUrl": "https://img.alicdn.com/img/ibank/O1CN01TfAMgq2KExhpOwxbE_!!2214687799526-0-cib.jpg",
  "images": [
    "https://img.alicdn.com/img/ibank/O1CN01TfAMgq2KExhpOwxbE_!!2214687799526-0-cib.jpg",
    "https://img.alicdn.com/img/ibank/O1CN01NhwImi2KExhrALHsS_!!2214687799526-0-cib.jpg"
  ],
  "skuMatrix": [
    {
      "skuId": "5066775858930",
      "specId": "5405c1ade1d9d2e9ba0c2ad101623132",
      "variant": "苹果X-XS【草紫色】",
      "price": 1.8,
      "stock": 4967,
      "imageUrl": "https://img.alicdn.com/img/ibank/O1CN01cn9PGM2KExhk07FyO_!!2214687799526-0-cib.jpg"
    },
    {
      "skuId": "4893701804460",
      "specId": "2b4174c3e987a9eca9a9c741f3c495ad",
      "variant": "苹果X-XS【石墨黑】",
      "price": 1.8,
      "stock": 4389,
      "imageUrl": "https://img.alicdn.com/img/ibank/O1CN01juMWTc2KExhpOvLom_!!2214687799526-0-cib.jpg"
    }
  ],
  "packaging": [
    {
      "skuId": "4893701804460",
      "variant": "苹果X-XS【石墨黑】",
      "weightGrams": 30.0,
      "lengthCm": 15.0,
      "widthCm": 8.0,
      "heightCm": 1.2,
      "volumeCm3": 144.0
    }
  ],
  "shipping": {
    "dispatchLocation": "广东省汕头市",
    "deliveryPromise": "承诺48小时发货",
    "dispatchTime": "预计2小时发货",
    "isFreeShipping": true
  },
  "supplier": {
    "companyName": "东莞市智造数码配件有限公司",
    "name": "东莞市智造数码配件有限公司",
    "city": "东莞市",
    "province": "广东省",
    "trustPass": true,
    "shopUrl": "https://winport.m.1688.com/page/index.html?memberId=b2b-220000000000000001"
  },
  "detailLevel": "full"
}
```

#### Frequently Asked Questions
**Q: Do I need a 1688 account, Chinese phone number, or cookies?**
No. The 1688 Wholesale Scraper runs 100% cookieless in the cloud. You never need a 1688 login, Alipay account, +86 SMS verification, or external proxies.

**Q: Can I search 1688 by product photo or image (以图搜款 / 拍立淘)?**
Yes! Use our dedicated 1688 Reverse Image Search Scraper (unitbytes/1688-image-search-scraper) to pass any Amazon, Shopify, or AliExpress product image URL and match it directly to verified Chinese OEM factories and MOQ price tiers.

**Q: What supplier and factory metrics are extracted?**
Every record includes tiered wholesale prices, SKU variant matrices, 30-day transaction volume, repeat buyer rate, factory verification badges (Super Factory / Bull Head), response rates, and unit weight/shipping dimensions.

**Q: Can I search in English or Chinese keywords?**
Yes. You can pass Chinese factory keywords, English product terms, direct 1688 search URLs, or specific 1688 product detail URLs and export flat CSV, Excel, or JSON.

---

### 🚀 1688 Image Search Scraper: Suppliers & Factories by Photo (`unitbytes/1688-image-search-scraper`)

<p align="center">
  <a href="https://apify.com/unitbytes/1688-image-search-scraper?fpr=939u3w&fp_sid=gh_1688" target="_blank">
    <img src="https://raw.githubusercontent.com/unitbytes/.github/main/assets/banners/unitbytes-1688-image-search-scraper-banner.jpg" alt="1688 Image Search Scraper: Suppliers & Factories by Photo" width="100%" />
  </a>
</p>

1688 image search & reverse image search API (from `$0.0009/item`). Find direct Chinese suppliers & factories on 1688.com by photo from Amazon FBA, Shopify, AliExpress & Alibaba. Extract wholesale prices, MOQ, SKU matrices & FBA weights with zero login.

- **Pricing:** `$0.0015 / item` (Pay-Per-Event — `$0.0015` visual match listing, `$0.0025` full b2b product detail & spec matrix (volume tiers from `$0.0009`))
- **Cloud Console:** [https://apify.com/unitbytes/1688-image-search-scraper?fpr=939u3w&fp_sid=gh_1688](https://apify.com/unitbytes/1688-image-search-scraper?fpr=939u3w&fp_sid=gh_1688)
- **Full Documentation & Schema:** [https://unitbytes.com/actors/1688-image-search-scraper/](https://unitbytes.com/actors/1688-image-search-scraper/)
- **n8n Workflow File:** [`n8n/1688-image-search-scraper-n8n-workflow.json`](n8n/1688-image-search-scraper-n8n-workflow.json)
- **Engineering Playbook:** [1688 Reverse Image Search & Alibaba B2B API Guide in 2026 (Photo-to-Factory Sourcing)](https://unitbytes.com/blog/1688-image-search-alibaba-b2b-supplier-api-sourcing-guide/)

#### Key Capabilities
- **Visual Photo-to-Factory Matching:** Pass any product image URL from Amazon, Shopify, AliExpress, or TikTok Shop (or Base64 image data) to discover exact OEM/ODM manufacturers on 1688.com.
- **Verified Factory & Super-Factory Filtering:** Automatically identifies verified manufacturers (生产加工), Super Factories, and on-site factory inspection badges to bypass trading middlemen.
- **Full SKU Matrices & Amazon FBA Weights:** Enriches visual matches with complete variant pricing, stock levels, and unit packaging dimensions/weights (weightGrams, volumeCm3) for instant landed-cost calculation.
- **Real-Time Standby HTTP API & n8n Ready:** Supports both batch Apify runs and sub-second Standby HTTP POST/GET requests for Chrome extensions, sourcing tools, and n8n automation pipelines.

#### ⚙️ Input Parameters (Schema)

| Parameter | Type | Default / Prefill | Description |
| :--- | :---: | :--- | :--- |
| `imageUrls` | `array` | `["https://img.alicdn.com/img/ibank/O1CN01gQo0hx2` | Paste one or more product image URLs (from Amazon, Shopify, AliExpress, TikTok Shop, eBay, or 1688) to find the original Chinese factories on 1688.com. |
| `imageFile` | `string` | — | Optional: Upload a local product photo (.jpg, .png, .webp) directly from your computer to match against 1688 factories. |
| `imagesBase64` | `array` | — | Optional list of Base64-encoded image strings or data:image/... URIs for automated API/ERP visual sourcing pipelines. |
| `maxItems` | `integer` | `30` | Maximum total number of matching wholesale offers to scrape across all images (1 to 10,000). |
| `maxResultsPerImage` | `integer` | — | Optional cap on how many matching 1688 factory offers to extract per input image when batch-processing multiple product photos. |
| `detailLevel` | `string` | `full` | Choose 'Full B2B Mode' for complete wholesale tiered volume prices, full color/size SKU variations, MOQ, Amazon FBA packaging weights, and verified factory audit badges, or 'Summary Mode' for fast visual match cards. |
| `sortBy` | `string` | `normal` | Sort visual matches by visual similarity ('normal'), highest factory sales volume ('booked'), or factory unit price ('priceAsc' / 'priceDesc'). |
| `superFactory` | `boolean` | `False` | Filter visual matches to verified 1688 Super Factories (超级工厂 / 实力认证) with high-capacity OEM/ODM production lines. |
| `factoryInspection` | `boolean` | `False` | Filter visual matches to manufacturers that have passed on-site third-party factory inspection (深度验厂 / 真实工厂认证). |
| `priceMin` | `integer` | — | Minimum unit wholesale price in Chinese Yuan (CNY ¥). Server-side filtered natively by 1688. |
| `priceMax` | `integer` | — | Maximum unit wholesale price in Chinese Yuan (CNY ¥). Server-side filtered natively by 1688. |
| `province` | `string` | — | Filter by Chinese manufacturing province (e.g. '广东' for Guangdong/Shenzhen/Guangzhou, '浙江' for Zhejiang/Yiwu/Hangzhou, '江苏' for Jiangsu). |
| `startUrls` | `array` | — | Optional: Paste 1688 visual search URLs ('https://s.1688.com/youyuan/index.htm?tab=imageSearch&imageId=...'), direct product image links, or direct 1688 offer links. |
| `resumptionToken` | `string` | — | Optional encrypted resumption token copied from a previous run, Key-Value store, or dataset item. Restores the exact session and continues scraping directly from where it left off. |
| `proxyConfiguration` | `object` | `{"useApifyProxy": true}` | Apify Proxy configuration for fast worldwide access. Apify Residential proxy is recommended for high-volume extraction. |

#### Python SDK Quickstart (`examples/run_1688_image_search_scraper.py`)
```python
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "imageUrls": [
        "https://img.alicdn.com/img/ibank/O1CN01gQo0hx2LY27U4AagC_!!3937219703-0-C2M.jpg"
    ],
    "maxItems": 30,
    "detailLevel": "full",
    "sortBy": "normal",
    "superFactory": False,
    "factoryInspection": False
}

run = client.actor("unitbytes/1688-image-search-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("price"), item.get("priceDisplay"))
```

#### Sample Output Schema (`samples/1688-image-search-scraper-sample.json`)
```json
{
  "id": "1030000000001",
  "offerId": "1030000000001",
  "searchType": "image",
  "searchImage": "https://img.alicdn.com/img/ibank/O1CN01gQo0hx2LY27U4AagC_!!3937219703-0-C2M.jpg",
  "imageId": "1393708864958124211",
  "imageSearchUrl": "https://s.1688.com/youyuan/index.htm?tab=imageSearch&imageId=1393708864958124211",
  "url": "https://detail.1688.com/offer/1030000000001.html",
  "title": "GTS15无线蓝牙耳机运动挂耳夹耳式新款适用华为索尼高音质降噪",
  "price": 20.9,
  "currency": "CNY",
  "priceDisplay": "20.90",
  "minOrderQuantity": 1,
  "totalStock": 79855,
  "salesVolume": "5800+件",
  "bookedCount": 1998,
  "repurchaseRate": "57%",
  "repurchasePct": 57.0,
  "superFactory": false,
  "factoryInspection": true,
  "bizType": "生产加工",
  "tieredPrices": [
    {
      "minQuantity": 1,
      "maxQuantity": null,
      "price": 20.9,
      "unit": "件"
    }
  ],
  "pictureUrl": "https://img.alicdn.com/img/ibank/O1CN01yQgnm028qjJjbUhrp_!!2212806287984-0-cib.jpg",
  "skuMatrix": [
    {
      "skuId": "6046270988275",
      "variant": "旗舰版【柏林音效+超长续航】肤色",
      "price": 20.9,
      "stock": 9998,
      "imageUrl": "https://img.alicdn.com/img/ibank/O1CN01yQgnm028qjJjbUhrp_!!2212806287984-0-cib.jpg"
    }
  ],
  "packaging": [
    {
      "skuId": "6046270988275",
      "variant": "旗舰版【柏林音效+超长续航】肤色",
      "weightGrams": 110.0,
      "lengthCm": 12.0,
      "widthCm": 9.0,
      "heightCm": 4.0,
      "volumeCm3": 432.0
    }
  ],
  "supplier": {
    "companyName": "深圳市创新声学电子有限公司",
    "name": "深圳市创新声学电子有限公司",
    "city": "深圳市",
    "province": "广东",
    "bizType": "生产加工",
    "trustPass": true,
    "shopUrl": "https://winport.m.1688.com/page/index.html?memberId=b2b-220000000000000002"
  },
  "detailLevel": "full"
}
```

#### Frequently Asked Questions
**Q: What image formats and URLs are supported for 1688 reverse image search?**
You can pass any public product photo URL (JPEG, PNG, WebP) from Amazon, Shopify, TikTok Shop, AliExpress, or Taobao into imageUrls, or upload an image directly in the Apify Console.

**Q: How does AI visual similarity ranking work?**
The engine submits your product photo directly to 1688's visual search index (拍立淘) and returns matching factory offers ranked by visual match confidence, 90-day order volume, and repeat buyer rate.

**Q: Does it extract verified OEM factory badges and MOQ pricing?**
Yes. Each visual match includes wholesale RMB price tiers, minimum order quantities (MOQ), 90-day transaction counts, province/city factory location, and verified manufacturer credentials.

**Q: Is there a synchronous REST API for real-time app integration?**
Yes. In addition to bulk cloud runs on Apify (`$0.0015`/match), you can call our synchronous 1688 REST Gateway on RapidAPI (`$0` Free / `$9` Pro) for sub-second responses.


---

## ⚡ Quick Installation & Local Usage

### 1. Run with Python (`apify-client`)
```bash
git clone https://github.com/unitbytes/1688-Wholesale-Scraper-API.git
cd 1688-Wholesale-Scraper-API
pip install -r requirements.txt
export APIFY_API_TOKEN="your_apify_api_token"
python examples/run_1688_scraper.py
```

### 2. Import into n8n (Self-Hosted or Cloud)
1. Open any `.json` file inside the [`n8n/`](n8n/) folder (or copy in 1 click from **[unitbytes.com/n8n](https://unitbytes.com/n8n/)** / **[n8n.io/creators/unitbytes](https://n8n.io/creators/unitbytes/)**).
2. Press **`Ctrl+V` / `Cmd+V`** directly onto your n8n workflow canvas.
3. Configure your Apify API Token in the `HTTP Header Auth` credential on Node `2. Run UnitBytes (...)` (and customize your search inputs in Node `1. Configure Search & Rules`), then click **Test Workflow**.

### 3. Use with AI Coding Agents (Cursor, Windsurf & Claude Code MCP)
This repository includes a ready-to-use Model Context Protocol configuration at [`.cursor/mcp.json`](.cursor/mcp.json) pointing to `https://mcp.apify.com` with this suite's UnitBytes actors pre-registered. Open this folder in **Cursor** or **Windsurf** to let your AI agent run live extractions and inspect schemas automatically.

---

## 💼 Need Done-For-You Datasets or Custom Pipelines?

Don't want to manage API tokens or scripts? **UnitBytes Data Delivery** provides ready-to-use **CSV, Excel (.xlsx), Google Sheets, or Webhook feeds** tailored to your exact target keywords, cities, or categories.

- 🌐 **Request a Sample Dataset:** [https://unitbytes.com/#enterprise-intake](https://unitbytes.com/#enterprise-intake)
- 📧 **Direct Engineering Contact:** [contact@unitbytes.com](mailto:contact@unitbytes.com)
- ⚡ **Explore All 39 Scrapers:** [https://unitbytes.com/actors/](https://unitbytes.com/actors/)
- 📚 **Engineering Playbooks & Guides:** [https://unitbytes.com/blog/](https://unitbytes.com/blog/)
- 🔗 **Official n8n Creator Profile:** [https://n8n.io/creators/unitbytes/](https://n8n.io/creators/unitbytes/)
