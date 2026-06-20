#!/usr/bin/env bash
# 빌드 후 모든 URL을 IndexNow(빙·네이버)에 즉시 통보한다.
set -e
cd "$(dirname "$0")/.."
python3 build.py
python3 tools/indexnow.py "$@"
