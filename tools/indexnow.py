#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — 빙(Bing)·네이버(Naver)·Yandex 등에 URL 변경을 알린다.

구글은 IndexNow에 참여하지 않으므로 이 스크립트로는 통보되지 않는다.
(구글은 Search Console 사이트맵 + tools/google_index.py 참고)

사용법:
  python tools/indexnow.py                 # sitemap.xml 의 모든 색인 URL 일괄 통보
  python tools/indexnow.py <url> [<url>..] # 지정한 URL만 통보 (새 글/수정 글 올릴 때)

사전 조건:
  1. content/site.py 의 BASE_URL 이 실제 서비스 도메인이어야 한다.
  2. python build.py 로 https://도메인/{INDEXNOW_KEY}.txt 키 파일이 배포돼 있어야 한다.
     (키 파일이 실제로 접근 가능해야 통보가 인증된다)
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

BASE = BASE_URL.rstrip("/")
HOST = urlparse(BASE).netloc
KEY = INDEXNOW_KEY
KEY_LOCATION = f"{BASE}/{KEY}.txt"

# IndexNow 참여 엔진 엔드포인트. 한 곳에 보내면 공유되지만,
# 빙·네이버 양쪽에 확실히 전달되도록 둘 다 직접 호출한다.
ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
    "https://searchadvisor.naver.com/indexnow",
]


def sitemap_urls():
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 `python build.py` 를 실행하세요.")
    xml = open(path, encoding="utf-8").read()
    return re.findall(r"<loc>(.*?)</loc>", xml)


def submit(urls):
    urls = [u for u in urls if u.startswith(BASE)]
    if not urls:
        sys.exit("통보할 URL 이 없습니다. (도메인이 BASE_URL 과 일치해야 합니다)")
    payload = json.dumps({
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }).encode("utf-8")

    print(f"IndexNow 통보 대상 {len(urls)}개 URL (host={HOST})")
    for ep in ENDPOINTS:
        req = urllib.request.Request(
            ep, data=payload,
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                print(f"  [{resp.status}] {ep}  (200/202 = 접수 성공)")
        except urllib.error.HTTPError as e:
            body = e.read()[:200].decode("utf-8", "ignore")
            print(f"  [{e.code}] {ep}  {body}")
        except Exception as e:  # noqa: BLE001
            print(f"  [ERR] {ep}  {e}")


if __name__ == "__main__":
    args = sys.argv[1:]
    urls = args if args else sitemap_urls()
    submit(urls)
