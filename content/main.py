# 메인 페이지 — 성동구 허브. 모든 키워드를 밀어 넣지 않고 상세 페이지로 연결한다.
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY, REGION_FULL
from .pricing import PRICING

# 네이버 서치어드바이저 사이트 소유확인 (루트 메인페이지)
_NAVER = '<meta name="naver-site-verification" content="fa2e95e8126651164aa2e31d93b8a7976a841212"/>\n'

_JSONLD = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{BRAND}",
  "telephone": "{PHONE}",
  "url": "{BASE_URL}/",
  "image": "{BASE_URL}/assets/og-image.png",
  "description": "성동구 전지역 방문 출장마사지·홈타이 예약 안내",
  "areaServed": {{
    "@type": "AdministrativeArea",
    "name": "{REGION_FULL}"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "성동구 출장마사지 · 성동구 홈타이 지역별 예약 안내",
  "url": "{BASE_URL}/",
  "inLanguage": "ko-KR",
  "primaryImageOfPage": {{
    "@type": "ImageObject",
    "url": "{BASE_URL}/assets/og-image.png",
    "width": 1200,
    "height": 630
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": "성동 홈", "item": "{BASE_URL}/" }}
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "성동구 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 지역별 안내에서 왕십리동, 성수동, 금호동, 옥수동, 행당동 등 대표동 기준으로 확인할 수 있습니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "왕십리역이나 성수역 근처도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "주요 역세권은 역 상세 페이지에서 인접 생활권과 함께 안내합니다. 환승역도 역명 기준 한 페이지로만 운영하며, 정확한 가능 여부는 예약 시 위치로 확인합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "성수1가동, 금호2가동은 왜 따로 없나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "번호로 나뉜 법정·행정동은 성수동·금호동·행당동·왕십리동 대표 페이지에서 세부 생활권으로 통합 안내하여 중복 페이지 위험을 줄입니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "추가 이동비가 있나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "지역과 예약 시간대, 이동 거리에 따라 추가 이동비가 발생할 수 있습니다. 기준은 예약 안내 페이지에서 확인하고 예약 시 최종 안내해 드립니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "홈타이와 출장마사지는 어떻게 다른가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "홈타이는 집에서 받는 방문형 관리의 한 형태이며, 출장마사지는 자택·숙소·사무실 인근으로 방문하는 서비스를 폭넓게 가리킵니다. 자세한 차이는 홈타이 이용 가이드에서 확인할 수 있습니다."
      }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Spa · 성동구 전지역</p>
    <h1>성동구 출장마사지·홈타이<br>지역별 예약 안내</h1>
    <p class="hero-lead">왕십리·성수·금호·옥수·행당까지, 계신 곳 가까운 생활권을 먼저 확인하세요.<br>자택·숙소·사무실 인근 어디든 전화 한 통이면 예약 가능 여부를 안내해 드립니다.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/seoul/seongdong/">지역별 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>10개</strong><span>대표동 안내</span></li>
      <li><strong>14개</strong><span>역세권 안내</span></li>
      <li><strong>10개</strong><span>생활권 안내</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<section id="standard">
<h2>성동구에서 출장마사지를 찾을 때 먼저 확인할 기준</h2>
<p>성동구 출장마사지를 찾는 분들은 보통 현재 위치에서 가장 가까운 방문 가능 지역부터 확인합니다. 성동구는 왕십리역을 중심으로 한 환승 생활권, 성수역과 서울숲 일대의 상권·업무 생활권, 금호동과 옥수동의 한강변 주거 생활권, 마장동과 용답동의 동부 생활권이 한 구 안에 함께 있습니다. 그래서 이 사이트는 "성동 전지역 가능"이라고만 적는 대신 대표동, 역세권, 생활권으로 나누어 안내합니다. 예약 전에는 방문 가능 주소, 예약 가능 시간, 추가 이동비, 결제 방식, 취소 기준, 개인정보 처리 기준을 먼저 확인하시는 것이 좋습니다. {BRAND}는 이 기준을 화면에 적힌 그대로 전화 상담에서도 동일하게 안내합니다.</p>
</section>

<section id="lifezone-diff">
<h2>왕십리·성수·금호·옥수 생활권 차이</h2>
<p>같은 성동구라도 생활권마다 분위기와 이동 조건이 다릅니다. 왕십리는 여러 노선이 만나는 환승 중심지로 검색 의도가 가장 넓고, 성수동은 카페거리·업무시설·주거지가 섞여 시간대별 유동이 큰 지역입니다. 금호동과 옥수동은 한강변 언덕 주거지라 차량 진입 경로 확인이 중요하고, 행당동과 사근동은 왕십리·한양대 생활권으로 연결됩니다. 마장동·송정동·용답동은 동부 생활권으로 묶어 차량 이동 기준을 더 자세히 안내합니다. 생활권 성격이 다르기 때문에 각 페이지를 그 지역 사실에 맞춰 따로 작성했습니다.</p>
</section>

<section id="areas">
<h2>대표동별 방문 가능 지역 안내</h2>
<p>대표동은 왕십리동, 마장동, 사근동, 행당동, 응봉동, 금호동, 옥수동, 성수동, 송정동, 용답동으로 구성합니다. 왕십리도선동·왕십리제2동은 왕십리동에서, 행당제1·2동은 행당동에서, 금호1가~4가동은 금호동에서, 성수1·2가의 행정동은 성수동에서 세부 생활권으로 통합 안내합니다. 거주하시거나 머무시는 동을 아래에서 선택해 주세요.</p>
<ul class="card-grid">
<li><a href="/seoul/seongdong/wangsimni-dong-chuljangmassage/">왕십리동 출장마사지</a></li>
<li><a href="/seoul/seongdong/seongsu-dong-chuljangmassage/">성수동 홈타이</a></li>
<li><a href="/seoul/seongdong/geumho-dong-chuljangmassage/">금호동 홈타이</a></li>
<li><a href="/seoul/seongdong/oksu-dong-chuljangmassage/">옥수동 홈타이</a></li>
<li><a href="/seoul/seongdong/haengdang-dong-chuljangmassage/">행당동 출장마사지</a></li>
<li><a href="/seoul/seongdong/majang-dong-chuljangmassage/">마장동 출장마사지</a></li>
<li><a href="/seoul/seongdong/sageun-dong-chuljangmassage/">사근동 출장마사지</a></li>
<li><a href="/seoul/seongdong/eungbong-dong-chuljangmassage/">응봉동 출장마사지</a></li>
<li><a href="/seoul/seongdong/songjeong-dong-chuljangmassage/">송정동 출장마사지</a></li>
<li><a href="/seoul/seongdong/yongdap-dong-chuljangmassage/">용답동 출장마사지</a></li>
</ul>
<p>성동구 전체 구조는 <a href="/seoul/seongdong/">지역별 안내</a>에서 한눈에 확인하실 수 있습니다.</p>
</section>

<section id="stations">
<h2>왕십리역·성수역·서울숲역·옥수역 역세권 안내</h2>
<p>역을 기준으로 위치를 설명하는 것이 익숙하시다면 역세권 안내를 참고하세요. 성동구를 지나는 2호선·5호선·경의중앙선·분당선·우이신설선 주요 역을 역마다 한 페이지씩 안내합니다. 왕십리역, 성수역, 옥수역, 금호역, 서울숲역처럼 노선이 여러 개인 역도 노선별로 쪼개지 않고 역명 기준 한 페이지로만 운영하며, 본문에서 환승 특징과 인접 생활권을 설명합니다.</p>
<ul class="card-grid">
<li><a href="/seoul/seongdong/wangsimni-station-chuljangmassage/">왕십리역 출장마사지</a></li>
<li><a href="/seoul/seongdong/sangwangsimni-station-chuljangmassage/">상왕십리역 출장마사지</a></li>
<li><a href="/seoul/seongdong/hanyang-univ-station-chuljangmassage/">한양대역 출장마사지</a></li>
<li><a href="/seoul/seongdong/seongsu-station-chuljangmassage/">성수역 홈타이</a></li>
<li><a href="/seoul/seongdong/ttukseom-station-chuljangmassage/">뚝섬역 출장마사지</a></li>
<li><a href="/seoul/seongdong/seoul-forest-station-chuljangmassage/">서울숲역 홈타이</a></li>
<li><a href="/seoul/seongdong/haengdang-station-chuljangmassage/">행당역 출장마사지</a></li>
<li><a href="/seoul/seongdong/eungbong-station-chuljangmassage/">응봉역 출장마사지</a></li>
<li><a href="/seoul/seongdong/geumho-station-chuljangmassage/">금호역 출장마사지</a></li>
<li><a href="/seoul/seongdong/singeumho-station-chuljangmassage/">신금호역 홈타이</a></li>
<li><a href="/seoul/seongdong/oksu-station-chuljangmassage/">옥수역 홈타이</a></li>
<li><a href="/seoul/seongdong/majang-station-chuljangmassage/">마장역 출장마사지</a></li>
<li><a href="/seoul/seongdong/sindap-station-chuljangmassage/">신답역 출장마사지</a></li>
<li><a href="/seoul/seongdong/yongdap-station-chuljangmassage/">용답역 출장마사지</a></li>
</ul>
<p>전체 역 목록은 <a href="/seoul/seongdong/stations/">역세권 안내</a>에서 확인하세요.</p>
</section>

<section id="lifezones">
<h2>생활권·주요 거점별 안내</h2>
<p>대표동·역세권과 별개로, 사람들이 실제로 묶어서 인식하는 생활권 단위 안내도 함께 제공합니다. 왕십리역 환승 생활권, 성수 카페거리, 서울숲·성수동1가, 뚝섬·성수 업무권, 금호·옥수 주거지, 행당·한양대처럼 이동 동선이 비슷한 권역을 정리했습니다.</p>
<ul class="card-grid">
<li><a href="/seoul/seongdong/wangsimni-transfer-area-chuljangmassage/">왕십리역 환승 생활권 출장마사지</a></li>
<li><a href="/seoul/seongdong/seongsu-cafe-street-area-chuljangmassage/">성수 카페거리 홈타이</a></li>
<li><a href="/seoul/seongdong/seoul-forest-seongsu1ga-area-chuljangmassage/">서울숲·성수동1가 출장마사지</a></li>
<li><a href="/seoul/seongdong/ttukseom-seongsu-business-area-chuljangmassage/">뚝섬·성수 업무권 출장마사지</a></li>
<li><a href="/seoul/seongdong/geumho-oksu-residential-area-chuljangmassage/">금호·옥수 주거지 홈타이</a></li>
<li><a href="/seoul/seongdong/haengdang-hanyang-univ-area-chuljangmassage/">행당동·한양대 출장마사지</a></li>
<li><a href="/seoul/seongdong/majang-market-area-chuljangmassage/">마장동 축산시장 출장마사지</a></li>
<li><a href="/seoul/seongdong/eungbong-mountain-area-chuljangmassage/">응봉동·응봉산 출장마사지</a></li>
<li><a href="/seoul/seongdong/yongdap-sindap-area-chuljangmassage/">용답동·신답역 출장마사지</a></li>
<li><a href="/seoul/seongdong/songjeong-jungnangcheon-area-chuljangmassage/">송정동·중랑천 홈타이</a></li>
</ul>
</section>

<section id="check">
<h2>성동구 홈타이 예약 전 확인사항</h2>
<p>성동구 홈타이는 자택, 숙소, 사무실 인근에서 예약 가능 여부를 확인한 뒤 이용하는 방문형 관리 서비스입니다. 송정동·용답동·금호동 일부 주거지는 시간대에 따라 차량 이동 기준이 달라질 수 있습니다. 예약 전에는 정확한 도로명 주소, 공동현관 출입 방법, 매트를 펼 공간, 조용한 환경을 확인해 주시면 좋습니다. 자세한 준비사항은 <a href="/check/">이용 전 확인사항</a>에, 홈타이 자체에 대한 설명은 <a href="/guide/">홈타이 이용 가이드</a>에 정리되어 있습니다.</p>
</section>

<section id="policy">
<h2>성동구 페이지 중복 방지 운영 기준</h2>
<p>이 사이트는 검색 순위를 위해 비슷한 페이지를 양산하지 않습니다. 왕십리도선동·왕십리제2동, 행당제1·2동, 금호1가~4가동, 성수1·2가의 세부 행정동은 각각 단독 페이지로 만들지 않고 대표동 본문 안에서 다룹니다. 환승역은 노선별로 쪼개지 않고 역명 기준 한 URL만 만들며, 답십리역·군자역·신당역처럼 인접 구 성격이 강한 역은 성동구 핵심 역세권으로 만들지 않습니다. 페이지 수보다 페이지마다의 정확도를 택한 구조입니다.</p>
</section>

<section id="how">
<h2>성동구 출장마사지 사이트 이용 방법</h2>
<p>이용 순서는 간단합니다. 먼저 대표동·역세권·생활권 안내 중 익숙한 기준으로 본인 위치를 확인하고, 예약 가능 시간과 추가 이동비 기준을 살핀 뒤, 전화로 위치와 희망 시간을 알려주시면 됩니다. 메인페이지는 성동구 전체 안내를, 대표동 페이지는 세부 동 검색을, 역세권 페이지는 실제 역 검색 수요를 담당합니다. 어느 페이지에서 출발하셔도 예약 기준은 같으니, 본인에게 편한 기준으로 보시면 됩니다.</p>
</section>

<section id="faq">
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>성동구 전지역 방문이 가능한가요?</h3>
<p>예약 시간과 정확한 위치, 배정 상황에 따라 달라집니다. 지역별 안내에서 왕십리·성수·금호·옥수·행당 등 대표동 기준으로 확인할 수 있습니다.</p>
</div>
<div class="faq-item">
<h3>왕십리역이나 성수역 근처도 가능한가요?</h3>
<p>주요 역세권은 역 상세 페이지에서 인접 생활권과 함께 안내합니다. 환승역도 역명 기준 한 페이지로만 운영합니다.</p>
</div>
<div class="faq-item">
<h3>성수1가동, 금호2가동은 왜 따로 없나요?</h3>
<p>번호로 나뉜 법정·행정동은 성수동·금호동·행당동·왕십리동 대표 페이지에서 세부 생활권으로 통합 안내해 중복을 줄입니다.</p>
</div>
<div class="faq-item">
<h3>추가 이동비가 있나요?</h3>
<p>지역·시간대·이동 거리에 따라 발생할 수 있으며, 기준은 <a href="/reservation/#fee">예약 안내</a>에서 확인하고 예약 시 최종 안내해 드립니다.</p>
</div>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>성동구 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "성동구 출장마사지｜왕십리·성수·옥수·금호 홈타이 지역 안내",
    "desc": "성동구 출장마사지·홈타이 예약 전 왕십리, 성수, 옥수, 금호, 행당 생활권을 확인하세요.",
    "h1": "성동구 출장마사지 · 성동구 홈타이 지역별 예약 안내",
    "body": _BODY,
    "extra_head": _NAVER + _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
