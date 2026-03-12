#!/usr/bin/env bash
set -euo pipefail

python -m erp_docs_mirror.cli crawl \
  --seed https://docs.frappe.io/erpnext/introduction \
  --seed https://docs.frappe.io/framework/user/en/introduction \
  --output ./output/full \
  --max-pages 50 \
  --delay 0.5

python -m erp_docs_mirror.cli validate --output ./output/full
