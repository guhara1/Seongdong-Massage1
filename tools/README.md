# 색인(인덱싱) 도구 — 가장 빠른 발견·색인 셋업

이 폴더는 새 글/수정 글을 검색엔진에 **즉시 통보**하기 위한 도구 모음입니다.

## 한눈에 보기

| 엔진 | 방법 | 즉시성 |
|------|------|--------|
| **빙(Bing)** | IndexNow (`indexnow.py`) | 즉시 |
| **네이버(Naver)** | IndexNow (`indexnow.py`) + 서치어드바이저 사이트맵 | 즉시 |
| **Yandex 등** | IndexNow (`indexnow.py`) | 즉시 |
| **구글(Google)** | Search Console 사이트맵 + URL 검사 (IndexNow 미참여) | 수동/반자동 |

> 구글은 IndexNow에 참여하지 않습니다. 일반 페이지의 구글 색인은 Search Console
> 사이트맵 제출 + URL 검사 '색인 생성 요청'이 가장 확실합니다. `google_index.py`는
> 보조 수단입니다(정책상 JobPosting/BroadcastEvent 전용 API라 효과 비보장).

## 0. 사전 준비 (최초 1회)

1. `content/site.py`의 `BASE_URL`이 실제 도메인인지 확인 → `python build.py`
2. 배포 후 다음이 실제로 열리는지 확인:
   - `https://<도메인>/sitemap.xml`
   - `https://<도메인>/rss.xml`
   - `https://<도메인>/c8b75f174737c8e8f6a65d19e839fd4e.txt` (IndexNow 키 파일, 내용 = 키)
3. **구글 Search Console** 속성 등록 → `sitemap.xml` 제출
4. **네이버 서치어드바이저** 사이트 등록(소유확인 메타는 메인에 이미 삽입) → `sitemap.xml`, `rss.xml` 제출
5. **빙 웹마스터도구**(선택) 사이트 등록 → 사이트맵 제출

## 1. 첫 일괄 통보 (사이트 전체)

```bash
python build.py            # 사이트맵·RSS·키 파일 최신화
python tools/indexnow.py   # sitemap.xml의 모든 URL을 빙·네이버에 즉시 통보
```

## 2. 글을 올리거나 수정할 때마다 (해당 URL만 즉시 통보)

```bash
python build.py
python tools/indexnow.py https://<도메인>/seoul/seongdong/<바뀐-페이지>/
# 여러 개도 가능:
python tools/indexnow.py "https://<도메인>/A/" "https://<도메인>/B/"
```

또는 빌드+전체 통보를 한 번에:

```bash
./tools/publish.sh
```

## 3. (옵션) 구글 Indexing API

`google_index.py` 상단 주석의 준비 절차(서비스 계정·권한·pip 설치)를 따른 뒤:

```bash
export GOOGLE_APPLICATION_CREDENTIALS=/path/service-account.json
python tools/google_index.py            # 전체
python tools/google_index.py <url> ...  # 지정 URL
```

## 참고 — 사이트맵 핑(ping)은 더 이상 동작하지 않습니다

구글·빙 모두 2023년에 `GET /ping?sitemap=` 엔드포인트를 폐기했습니다.
지금은 **IndexNow(빙·네이버)** 와 **Search Console 사이트맵 제출(구글)** 이 표준입니다.
