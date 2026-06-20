# 바로GO — 성동구 출장마사지·홈타이 안내 사이트

서울 성동구 전지역 방문 관리(출장마사지·홈타이) 안내용 정적 사이트입니다.
예약전화: **0508-202-4719**

## 구조

- 정적 HTML 사이트 — 어느 호스팅(GitHub Pages, Netlify, 일반 웹서버)에서든 그대로 서빙 가능
- `build.py` + `content/` 패키지에서 페이지를 생성하는 빌드 방식
- 생성물(각 디렉터리의 `index.html`, `sitemap.xml`, `robots.txt`)도 저장소에 포함

```
build.py            # 빌드 스크립트 (레이아웃·글자수 검사·sitemap 생성)
content/
  site.py           # 상호(바로GO)·전화·BASE_URL·메뉴 구조
  main.py           # 메인 페이지 (+ Organization/WebPage/FAQPage JSON-LD)
  areas.py          # 지역별: 성동구 허브 + 대표동 10개
  stations.py       # 역세권: 허브 + 14개 역
  lifezones.py      # 생활권: 허브 + 10개 생활권
  info.py           # 예약·이용 전 확인사항·홈타이 가이드·고객센터·약관
  about.py          # 사이트 소개 (E-E-A-T)
  pricing.py        # 공용 요금 블록
assets/             # CSS(프리미엄 팔레트 + Pretendard), 모바일 내비 JS, 파비콘/OG
```

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수 리포트가 출력됩니다.

## SEO 운영 원칙 (빌드에 강제됨)

- 본문 **2,000자 미만 페이지는 자동 `noindex`** 처리되고 sitemap에서 제외
- 대표동은 10개(왕십리·마장·사근·행당·응봉·금호·옥수·성수·송정·용답) — 번호 행정동 페이지 없음
  - 왕십리도선동·왕십리제2동 → 왕십리동 / 행당제1·2동 → 행당동
  - 금호1가~4가동 → 금호동 / 성수1·2가 행정동 → 성수동 으로 통합
- 역은 역명 기준 1개 URL — 환승역(왕십리·성수·옥수·금호)도 노선별로 쪼개지 않음
- 답십리·군자·신당역은 인접 구 성격이 강해 성동구 핵심 역세권으로 만들지 않음
- 지역+역+테마 조합 페이지 없음 (도어웨이 방지)
- 모든 페이지 본문은 페이지별 고유 작성 (지역명만 바꾼 복붙 없음)
- 불법·선정적 표현, 허위 후기, 과도한 할인 문구 미사용

## 디자인

- 프리미엄 팔레트: 웜 옵시디언 + 샴페인 골드 (`assets/style.css`의 디자인 토큰)
- 본문 Pretendard, 디스플레이 헤딩 Noto Serif KR
- 컴포넌트 오버레이: 히어로 격자 텍스처, 섹션 상단 골드 시닝, 카드 호버 글로우

## 배포 전 해야 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경
2. `python3 build.py` 재실행 (canonical·sitemap·robots.txt에 반영됨)
3. Google Search Console / 네이버 서치어드바이저에 `sitemap.xml` 제출
