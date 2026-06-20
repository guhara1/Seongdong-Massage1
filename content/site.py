# 사이트 공통 설정
# 배포 도메인 확정 후 BASE_URL 을 실제 도메인으로 변경하세요.
BASE_URL = "https://seongdong-massage1.pages.dev"

BRAND = "바로GO"
BRAND_MARK = "바로"          # 헤더 원형 마크 글자
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

REGION = "성동구"            # 서비스 대상 행정구
REGION_FULL = "서울특별시 성동구"

# 상단 메뉴 — 하위 메뉴에는 키워드를 반복하지 않고 지역명·역명만 표시한다.
NAV = [
    ("성동 홈", "/", []),
    ("지역별 안내", "/seoul/seongdong/", [
        ("성동구 전체", "/seoul/seongdong/"),
        ("왕십리동", "/seoul/seongdong/wangsimni-dong-chuljangmassage/"),
        ("마장동", "/seoul/seongdong/majang-dong-chuljangmassage/"),
        ("사근동", "/seoul/seongdong/sageun-dong-chuljangmassage/"),
        ("행당동", "/seoul/seongdong/haengdang-dong-chuljangmassage/"),
        ("응봉동", "/seoul/seongdong/eungbong-dong-chuljangmassage/"),
        ("금호동", "/seoul/seongdong/geumho-dong-chuljangmassage/"),
        ("옥수동", "/seoul/seongdong/oksu-dong-chuljangmassage/"),
        ("성수동", "/seoul/seongdong/seongsu-dong-chuljangmassage/"),
        ("송정동", "/seoul/seongdong/songjeong-dong-chuljangmassage/"),
        ("용답동", "/seoul/seongdong/yongdap-dong-chuljangmassage/"),
    ]),
    ("역세권 안내", "/seoul/seongdong/stations/", [
        ("역 전체", "/seoul/seongdong/stations/"),
        ("왕십리역", "/seoul/seongdong/wangsimni-station-chuljangmassage/"),
        ("상왕십리역", "/seoul/seongdong/sangwangsimni-station-chuljangmassage/"),
        ("한양대역", "/seoul/seongdong/hanyang-univ-station-chuljangmassage/"),
        ("뚝섬역", "/seoul/seongdong/ttukseom-station-chuljangmassage/"),
        ("성수역", "/seoul/seongdong/seongsu-station-chuljangmassage/"),
        ("서울숲역", "/seoul/seongdong/seoul-forest-station-chuljangmassage/"),
        ("마장역", "/seoul/seongdong/majang-station-chuljangmassage/"),
        ("신답역", "/seoul/seongdong/sindap-station-chuljangmassage/"),
        ("용답역", "/seoul/seongdong/yongdap-station-chuljangmassage/"),
        ("행당역", "/seoul/seongdong/haengdang-station-chuljangmassage/"),
        ("응봉역", "/seoul/seongdong/eungbong-station-chuljangmassage/"),
        ("금호역", "/seoul/seongdong/geumho-station-chuljangmassage/"),
        ("신금호역", "/seoul/seongdong/singeumho-station-chuljangmassage/"),
        ("옥수역", "/seoul/seongdong/oksu-station-chuljangmassage/"),
    ]),
    ("생활권 안내", "/seoul/seongdong/areas/", [
        ("생활권 전체", "/seoul/seongdong/areas/"),
        ("왕십리역 환승 생활권", "/seoul/seongdong/wangsimni-transfer-area-chuljangmassage/"),
        ("성수 카페거리", "/seoul/seongdong/seongsu-cafe-street-area-chuljangmassage/"),
        ("서울숲·성수동1가", "/seoul/seongdong/seoul-forest-seongsu1ga-area-chuljangmassage/"),
        ("뚝섬·성수 업무권", "/seoul/seongdong/ttukseom-seongsu-business-area-chuljangmassage/"),
        ("금호·옥수 주거지", "/seoul/seongdong/geumho-oksu-residential-area-chuljangmassage/"),
        ("행당·한양대", "/seoul/seongdong/haengdang-hanyang-univ-area-chuljangmassage/"),
        ("마장동 축산시장", "/seoul/seongdong/majang-market-area-chuljangmassage/"),
        ("응봉동·응봉산", "/seoul/seongdong/eungbong-mountain-area-chuljangmassage/"),
        ("용답동·신답역", "/seoul/seongdong/yongdap-sindap-area-chuljangmassage/"),
        ("송정동·중랑천", "/seoul/seongdong/songjeong-jungnangcheon-area-chuljangmassage/"),
    ]),
    ("예약 안내", "/reservation/", [
        ("예약 방법", "/reservation/#how"),
        ("예약 가능 시간", "/reservation/#hours"),
        ("방문 가능 장소", "/reservation/#place"),
        ("추가 이동비 안내", "/reservation/#fee"),
        ("결제 안내", "/reservation/#payment"),
        ("변경·취소 안내", "/reservation/#change"),
    ]),
    ("이용 전 확인사항", "/check/", [
        ("방문 가능 주소 확인", "/check/#address"),
        ("자택 이용 전 확인", "/check/#home"),
        ("숙소 이용 전 확인", "/check/#stay"),
        ("사무실 인근 이용 전 확인", "/check/#office"),
        ("개인정보 처리 기준", "/check/#privacy"),
        ("고객 안전 안내", "/check/#safety"),
    ]),
    ("홈타이 이용 가이드", "/guide/", [
        ("홈타이란?", "/guide/#what"),
        ("출장마사지와 홈타이 차이", "/guide/#diff"),
        ("성동구 이용 전 기준", "/guide/#standard"),
        ("지역별 이동 기준", "/guide/#move"),
        ("추가 비용 확인 기준", "/guide/#cost"),
        ("처음 이용하는 고객 안내", "/guide/#first"),
    ]),
    ("고객센터", "/support/", [
        ("문의하기", "/support/#contact"),
        ("자주 묻는 질문", "/support/#faq"),
        ("운영 기준", "/support/#policy"),
        ("사이트 소개", "/about/"),
        ("개인정보 처리방침", "/support/privacy/"),
        ("이용약관", "/support/terms/"),
    ]),
]
