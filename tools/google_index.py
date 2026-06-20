#!/usr/bin/env python3
"""(옵션) 구글 Indexing API 통보.

⚠️ 주의: 구글 Indexing API 는 공식적으로 JobPosting·BroadcastEvent 구조화 데이터
페이지만 지원합니다. 일반 페이지 색인 요청에 사용하는 것은 구글 정책상 권장되지
않으며 효과가 보장되지 않습니다. 일반 페이지의 가장 확실한 구글 색인 경로는:
  1) Search Console 에 sitemap.xml 제출
  2) URL 검사 → '색인 생성 요청'
입니다. 이 스크립트는 보조 수단으로만 사용하세요.

사전 준비:
  1. Google Cloud 프로젝트에서 'Indexing API' 사용 설정
  2. 서비스 계정 생성 → JSON 키 다운로드
  3. Search Console 속성에 그 서비스 계정 이메일을 '소유자'로 추가
  4. pip install google-auth requests
  5. 환경변수 GOOGLE_APPLICATION_CREDENTIALS=서비스계정.json 설정

사용법:
  python tools/google_index.py                  # sitemap.xml 의 모든 URL
  python tools/google_index.py <url> [<url>..]  # 지정 URL만
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]


def sitemap_urls():
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 `python build.py` 를 실행하세요.")
    return re.findall(r"<loc>(.*?)</loc>", open(path, encoding="utf-8").read())


def main(urls):
    try:
        from google.oauth2 import service_account
        from google.auth.transport.requests import AuthorizedSession
    except ImportError:
        sys.exit("의존성이 없습니다.  pip install google-auth requests  후 다시 실행하세요.")

    cred_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred_path or not os.path.exists(cred_path):
        sys.exit("GOOGLE_APPLICATION_CREDENTIALS 환경변수에 서비스계정 JSON 경로를 지정하세요.")

    creds = service_account.Credentials.from_service_account_file(cred_path, scopes=SCOPES)
    session = AuthorizedSession(creds)

    print(f"구글 Indexing API 통보 {len(urls)}개 URL")
    for url in urls:
        body = {"url": url, "type": "URL_UPDATED"}
        r = session.post(ENDPOINT, json=body, timeout=30)
        print(f"  [{r.status_code}] {url}")


if __name__ == "__main__":
    args = sys.argv[1:]
    main(args if args else sitemap_urls())
