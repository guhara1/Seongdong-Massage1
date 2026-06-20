# 내부링크 메시 — 지역·역·생활권 페이지에 '이웃 지역' 관련 링크 블록을 붙인다.
# 모든 지역 페이지 URL은 /seoul/seongdong/{slug}-chuljangmassage/ 형태로 통일돼 있다.

LABELS = {
    # 대표동
    "wangsimni-dong": "왕십리동", "majang-dong": "마장동", "sageun-dong": "사근동",
    "haengdang-dong": "행당동", "eungbong-dong": "응봉동", "geumho-dong": "금호동",
    "oksu-dong": "옥수동", "seongsu-dong": "성수동", "songjeong-dong": "송정동",
    "yongdap-dong": "용답동",
    # 역세권
    "wangsimni-station": "왕십리역", "sangwangsimni-station": "상왕십리역",
    "hanyang-univ-station": "한양대역", "ttukseom-station": "뚝섬역",
    "seongsu-station": "성수역", "seoul-forest-station": "서울숲역",
    "majang-station": "마장역", "sindap-station": "신답역", "yongdap-station": "용답역",
    "haengdang-station": "행당역", "eungbong-station": "응봉역", "geumho-station": "금호역",
    "singeumho-station": "신금호역", "oksu-station": "옥수역",
    # 생활권
    "wangsimni-transfer-area": "왕십리역 환승", "seongsu-cafe-street-area": "성수 카페거리",
    "seoul-forest-seongsu1ga-area": "서울숲·성수1가", "ttukseom-seongsu-business-area": "뚝섬·성수 업무권",
    "geumho-oksu-residential-area": "금호·옥수 주거지", "haengdang-hanyang-univ-area": "행당·한양대",
    "majang-market-area": "마장동 축산시장", "eungbong-mountain-area": "응봉동·응봉산",
    "yongdap-sindap-area": "용답동·신답역", "songjeong-jungnangcheon-area": "송정동·중랑천",
}

# 페이지별 이웃(인접 생활권) 관련 링크 — 대표동·역·생활권을 섞어 5개씩 큐레이션
RELATED = {
    # ── 대표동 ──
    "wangsimni-dong": ["haengdang-dong", "wangsimni-station", "sangwangsimni-station", "wangsimni-transfer-area", "majang-dong"],
    "majang-dong": ["majang-station", "majang-market-area", "yongdap-dong", "sageun-dong", "wangsimni-dong"],
    "sageun-dong": ["hanyang-univ-station", "haengdang-dong", "haengdang-hanyang-univ-area", "wangsimni-dong", "majang-dong"],
    "haengdang-dong": ["haengdang-station", "wangsimni-station", "hanyang-univ-station", "haengdang-hanyang-univ-area", "wangsimni-dong"],
    "eungbong-dong": ["eungbong-station", "eungbong-mountain-area", "geumho-dong", "oksu-dong", "haengdang-dong"],
    "geumho-dong": ["geumho-station", "singeumho-station", "geumho-oksu-residential-area", "oksu-dong", "eungbong-dong"],
    "oksu-dong": ["oksu-station", "geumho-dong", "geumho-oksu-residential-area", "eungbong-dong", "eungbong-station"],
    "seongsu-dong": ["seongsu-station", "ttukseom-station", "seoul-forest-station", "seongsu-cafe-street-area", "seoul-forest-seongsu1ga-area"],
    "songjeong-dong": ["songjeong-jungnangcheon-area", "seongsu-dong", "yongdap-dong", "seongsu-station", "ttukseom-seongsu-business-area"],
    "yongdap-dong": ["yongdap-station", "sindap-station", "yongdap-sindap-area", "majang-dong", "songjeong-dong"],
    # ── 역세권 ──
    "wangsimni-station": ["wangsimni-dong", "haengdang-dong", "sangwangsimni-station", "wangsimni-transfer-area", "haengdang-station"],
    "sangwangsimni-station": ["wangsimni-dong", "wangsimni-station", "wangsimni-transfer-area", "haengdang-dong", "hanyang-univ-station"],
    "hanyang-univ-station": ["sageun-dong", "haengdang-dong", "haengdang-station", "haengdang-hanyang-univ-area", "wangsimni-station"],
    "ttukseom-station": ["seongsu-dong", "seoul-forest-station", "seongsu-station", "seoul-forest-seongsu1ga-area", "ttukseom-seongsu-business-area"],
    "seongsu-station": ["seongsu-dong", "ttukseom-station", "seoul-forest-station", "seongsu-cafe-street-area", "songjeong-dong"],
    "seoul-forest-station": ["seongsu-dong", "ttukseom-station", "seoul-forest-seongsu1ga-area", "seongsu-station", "seongsu-cafe-street-area"],
    "majang-station": ["majang-dong", "majang-market-area", "yongdap-station", "yongdap-dong", "sindap-station"],
    "sindap-station": ["yongdap-dong", "yongdap-station", "yongdap-sindap-area", "majang-station", "majang-dong"],
    "yongdap-station": ["yongdap-dong", "sindap-station", "yongdap-sindap-area", "majang-dong", "majang-station"],
    "haengdang-station": ["haengdang-dong", "wangsimni-station", "hanyang-univ-station", "haengdang-hanyang-univ-area", "wangsimni-dong"],
    "eungbong-station": ["eungbong-dong", "eungbong-mountain-area", "geumho-station", "geumho-dong", "haengdang-dong"],
    "geumho-station": ["geumho-dong", "singeumho-station", "geumho-oksu-residential-area", "oksu-station", "oksu-dong"],
    "singeumho-station": ["geumho-dong", "geumho-station", "haengdang-dong", "geumho-oksu-residential-area", "haengdang-station"],
    "oksu-station": ["oksu-dong", "geumho-station", "geumho-oksu-residential-area", "geumho-dong", "eungbong-station"],
    # ── 생활권 ──
    "wangsimni-transfer-area": ["wangsimni-dong", "haengdang-dong", "wangsimni-station", "sangwangsimni-station", "haengdang-hanyang-univ-area"],
    "seongsu-cafe-street-area": ["seongsu-dong", "seongsu-station", "ttukseom-station", "seoul-forest-seongsu1ga-area", "ttukseom-seongsu-business-area"],
    "seoul-forest-seongsu1ga-area": ["seongsu-dong", "seoul-forest-station", "ttukseom-station", "seongsu-cafe-street-area", "seongsu-station"],
    "ttukseom-seongsu-business-area": ["seongsu-dong", "ttukseom-station", "seongsu-station", "seongsu-cafe-street-area", "songjeong-dong"],
    "geumho-oksu-residential-area": ["geumho-dong", "oksu-dong", "geumho-station", "oksu-station", "eungbong-dong"],
    "haengdang-hanyang-univ-area": ["haengdang-dong", "sageun-dong", "haengdang-station", "hanyang-univ-station", "wangsimni-dong"],
    "majang-market-area": ["majang-dong", "majang-station", "yongdap-dong", "yongdap-sindap-area", "sageun-dong"],
    "eungbong-mountain-area": ["eungbong-dong", "eungbong-station", "geumho-dong", "geumho-oksu-residential-area", "oksu-dong"],
    "yongdap-sindap-area": ["yongdap-dong", "yongdap-station", "sindap-station", "majang-dong", "majang-market-area"],
    "songjeong-jungnangcheon-area": ["songjeong-dong", "seongsu-dong", "seongsu-station", "yongdap-dong", "ttukseom-seongsu-business-area"],
}

# 무결성 검사 — 잘못된 슬러그가 있으면 빌드 시 즉시 드러난다.
for _s, _lst in RELATED.items():
    assert _s in LABELS, f"unknown source slug: {_s}"
    for _t in _lst:
        assert _t in LABELS, f"unknown target slug: {_t} (in {_s})"

_HEADING = {
    "dong": "이웃 대표동·역세권 안내",
    "station": "인근 역·대표동 안내",
    "area": "주변 생활권·역세권 안내",
}


def related_block(slug, kind="dong"):
    """페이지에 붙는 '이웃 지역' 관련 링크 카드 블록."""
    items = RELATED.get(slug, [])
    lis = "".join(
        f'<li><a href="/seoul/seongdong/{s}-chuljangmassage/">{LABELS[s]}</a></li>'
        for s in items
    )
    heading = _HEADING.get(kind, _HEADING["dong"])
    return f"""
<section>
<h2>{heading}</h2>
<ul class="card-grid">{lis}</ul>
</section>
"""
