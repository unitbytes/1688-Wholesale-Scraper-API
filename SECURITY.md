# Security Policy

## Supported Versions

All UnitBytes Python SDK quickstarts, n8n workflow templates, and cloud data extraction APIs in this repository are actively maintained and monitored.

| Component | Supported |
| :--- | :--- |
| Cloud API & Apify Actors (`unitbytes/*`) | ✅ Active |
| Python SDK Quickstarts (`examples/*.py`) | ✅ Active |
| n8n Workflow Templates (`n8n/*.json`) | ✅ Active |

## Credential & Token Safety

- **Never commit API tokens or credentials:** Always supply your `APIFY_API_TOKEN` via environment variables (`export APIFY_API_TOKEN="..."`) rather than hardcoding tokens in scripts or `.json` workflow files.
- **Zero-Cookie Architecture:** UnitBytes cloud actors run without requiring personal platform cookies, SMS logins, or session credentials.

## Reporting a Vulnerability

If you discover a security issue or credential exposure, please report it privately to:
- **Email:** [contact@unitbytes.com](mailto:contact@unitbytes.com)
- **Website:** [https://unitbytes.com](https://unitbytes.com)
