#!/usr/bin/env bash
set -euo pipefail

export PYTHONPATH=src

python -m erp_docs_mirror.cli crawl \
  --seed https://docs.frappe.io/erpnext/introduction \
  --seed https://docs.frappe.io/framework/user/en/introduction \
  --output ./output/full \
  --allowed-prefix /erpnext/ \
  --allowed-prefix /framework/ \
  --max-pages 100 \
  --delay 0.2

python -m erp_docs_mirror.cli validate --output ./output/full
