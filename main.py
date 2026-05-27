import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="MBTI 포켓몬 추천기 ✨",
    page_icon="⚡",
    layout="centered"
)

# MBTI별 포켓몬 데이터 (각 MBTI마다 5마리씩!)
mbti_pokemon = {
    "INTJ": {
        "personality": "냉철한 전략가 🎯",
        "color": "#8B5CF6",
        "pokemons": [
            {"name": "뮤츠", "id": 150, "desc": "강력한 사이코 파워로 모든 것을 꿰뚫어보는 천재형 포켓몬!"},
            {"name": "기라티나", "id": 487, "desc": "다른 차원에서 온 신비로운 존재. 깊은 사고의 소유자!"},
            {"name": "메타그로스", "id": 376, "desc": "슈퍼컴퓨터를 능가하는 두뇌를 가진 전략가!"},
            {"name": "다크라이", "id": 491, "desc": "그림자 속에서 조용히 계획을 세우는 신비주의자!"},
            {"name": "지가르데", "id": 718, "desc": "질서를 수호하는 논리적인 전설의 포켓몬!"},
        ]
    },
    "INTP": {
        "personality": "탐구하는 학자 📚",
        "color": "#FBBF24",
        "pokemons": [
            {"name": "알라카잠", "id": 65, "desc": "IQ 5000! 끊임없이 사색하는 천재 포켓몬!"},
            {"name": "포리곤Z", "id": 474, "desc": "디지털 세계를 탐구하는 호기심 많은 포켓몬!"},
            {"name": "뮤", "id": 151, "desc": "모든 포켓몬의 유전자를 가진 신비한 탐구자!"},
            {"name": "유크시", "id": 480, "desc": "지식의 화신, 인류에게 지혜를 준 전설!"},
            {"name": "프리져", "id": 144, "desc": "차갑고 이성적인 분석가의 모습!"},
        ]
    },
    "ENTJ": {
        "personality": "타고난 지휘관 👑",
        "color": "#EF4444",
        "pokemons": [
            {"name": "리자몽", "id": 6, "desc": "하늘을 지배하는 카리스마 넘치는 리더!"},
            {"name": "가이오가", "id": 382, "desc": "바다를 다스리는 강력한 통솔자!"},
            {"name": "삼삼드래", "id": 635, "desc": "세 개의 머리로 적을 압도하는 지휘관!"},
            {"name": "이벨타르", "id": 717, "desc": "파괴의 전설, 강력한 카리스마의 화신!"},
            {"name": "어그론", "id": 306, "desc": "강철 같은 의지로 영역을 지키는 리더!"},
        ]
    },
    "ENTP": {
        "personality": "혁신적인 발명가 🚀",
        "color": "#A78BFA",
        "pokemons": [
            {"name": "겟핸보숭", "id": 424, "desc": "재치 넘치는 손재주의 달인!"},
            {"name": "로토무", "id": 479, "desc": "다양한 모습으로 변신하는 창의왕!"},
            {"name": "조로아크", "id": 571, "desc": "환술의 마스터, 기발한 아이디어 뱅크!"},
            {"name": "후파", "id": 720, "desc": "장난기 가득한 트릭스터!"},
            {"name": "에이팜", "id": 190, "desc": "꼬리까지 활용하는 멀티 플레이어!"},
        ]
    },
    "INFJ": {
        "personality": "신비로운 예언자 🔮",
        "color": "#3B82F6",
        "pokemons": [
            {"name": "루카리오", "id": 448, "desc": "파동을 읽어 마음을 꿰뚫는 통찰가!"},
            {"name": "가디안", "id": 282, "desc": "주인을 위해 미래를 예측하는 수호자!"},
            {"name": "크레세리아", "id": 488, "desc": "달빛처럼 신비로운 치유의 전설!"},
            {"name": "샤미드", "id": 197, "desc": "달의 기운을 받은 우아한 직관가!"},
            {"name": "엠펠도", "id": 395, "desc": "고독하지만 깊은 신념의 황제!"},
        ]
    },
    "INFP": {
        "personality": "꿈꾸는 이상주의자 🌸",
        "color": "#F472B6",
        "pokemons": [
            {"name": "이브이", "id": 133, "desc": "무한한 가능성을 품은 순수한 영혼!"},
            {"name": "님피아", "id": 700, "desc": "사랑의 리본으로 평화를 전하는 천사!"},
            {"name": "프시아나", "id": 196, "desc": "햇살처럼 따뜻한 마음의 소유자!"},
            {"name": "셀레비", "id": 251, "desc": "시간을 넘나드는 숲의 요정!"},
            {"name": "라티아스", "id": 380, "desc": "감수성 풍부한 마음의 포켓몬!"},
        ]
    },
    "ENFJ": {
        "personality": "따뜻한 선도자 🌈",
        "color": "#EC4899",
        "pokemons": [
            {"name": "푸린", "id": 39, "desc": "노래로 모두를 행복하게 하는 매력쟁이!"},
            {"name": "블래키", "id": 197, "desc": "주인에게 헌신하는 충실한 동반자!"},
            {"name": "메로엣타", "id": 648, "desc": "음악으로 사람들의 감정을 어루만지는 가수!"},
            {"name": "킬가르도", "id": 681, "desc": "왕을 보좌하는 충직한 리더!"},
            {"name": "비크티니", "id": 494, "desc": "승리를 부르는 희망의 전령!"},
        ]
    },
    "ENFP": {
        "personality": "활기찬 모험가 🎉",
        "color": "#FCD34D",
        "pokemons": [
            {"name": "피카츄", "id": 25, "desc": "에너지 넘치는 모두의 친구!"},
            {"name": "마릴", "id": 183, "desc": "통통 튀는 귀여운 활동가!"},
            {"name": "토게피", "id": 175, "desc": "행복을 나눠주는 긍정 에너지!"},
            {"name": "데덴네", "id": 702, "desc": "전기처럼 짜릿한 매력의 소유자!"},
            {"name": "치라치노", "id": 573, "desc": "반짝반짝 빛나는 사교왕!"},
        ]
    },
    "ISTJ": {
        "personality": "신뢰의 수호자 🏛️",
        "color": "#60A5FA",
        "pokemons": [
            {"name": "꼬부기", "id": 7, "desc": "단단한 등껍질로 신뢰를 지키는 포켓몬!"},
            {"name": "거북왕", "id": 9, "desc": "냉정하고 침착한 베테랑!"},
            {"name": "메타그로스", "id": 376, "desc": "체계적이고 논리적인 강철 두뇌!"},
            {"name": "레지락", "id": 377, "desc": "변치 않는 바위처럼 견고한 신뢰감!"},
            {"name": "딘러스", "id": 208, "desc": "강철 같은 의지의 수호자!"},
        ]
    },
    "ISFJ": {
        "personality": "헌신적인 수호자 🌱",
        "color": "#34D399",
        "pokemons": [
            {"name": "치코리타", "id": 152, "desc": "향기로 치유를 주는 따뜻한 친구!"},
            {"name": "해피너스", "id": 242, "desc": "행복을 나눠주는 다정한 천사!"},
            {"name": "럭키", "id": 113, "desc": "아픈 이를 보살피는 헌신의 화신!"},
            {"name": "마릴리", "id": 184, "desc": "가족을 지키는 사랑스러운 보호자!"},
            {"name": "솜솜코", "id": 187, "desc": "부드럽게 주변을 감싸는 다정함!"},
        ]
    },
    "ESTJ": {
        "personality": "체계적인 관리자 💼",
        "color": "#6B7280",
        "pokemons": [
            {"name": "괴력몬", "id": 68, "desc": "강력한 힘으로 조직을 이끄는 리더!"},
            {"name": "딱구리", "id": 248, "desc": "확실한 카리스마의 대장!"},
            {"name": "한카리아스", "id": 445, "desc": "압도적인 실행력의 소유자!"},
            {"name": "메타그로스", "id": 376, "desc": "체계와 논리의 마스터!"},
            {"name": "디아루가", "id": 483, "desc": "시간의 질서를 지키는 통치자!"},
        ]
    },
    "ESFJ": {
        "personality": "사교적인 외교관 🤝",
        "color": "#FBCFE8",
        "pokemons": [
            {"name": "해피너스", "id": 242, "desc": "모두를 챙기는 따뜻한 천사!"},
            {"name": "푸크린", "id": 40, "desc": "사랑스러운 분위기 메이커!"},
            {"name": "라프라스", "id": 131, "desc": "친절하고 다정한 바다의 친구!"},
            {"name": "키링키", "id": 203, "desc": "두 마음으로 모두를 배려하는 사교왕!"},
            {"name": "또도가스", "id": 110, "desc": "주변을 즐겁게 하는 분위기 메이커!"},
        ]
    },
    "ISTP": {
        "personality": "쿨한 장인 🔧",
        "color": "#1E40AF",
        "pokemons": [
            {"name": "갸라도스", "id": 130, "desc": "조용하지만 강력한 카리스마!"},
            {"name": "루카리오", "id": 448, "desc": "차분하면서도 실력파인 무도가!"},
            {"name": "쉐이미", "id": 492, "desc": "독립적이고 자유로운 영혼!"},
            {"name": "절각참", "id": 123, "desc": "날카로운 기술의 검술 마스터!"},
            {"name": "마기라스", "id": 248, "desc": "고독한 강자의 카리스마!"},
        ]
    },
    "ISFP": {
        "personality": "예술적인 모험가 🎨",
        "color": "#86EFAC",
        "pokemons": [
            {"name": "이상해씨", "id": 1, "desc": "등에 꽃을 피우는 예술적인 영혼!"},
            {"name": "리피아", "id": 470, "desc": "자연과 하나되는 평화로운 포켓몬!"},
            {"name": "비크티니", "id": 494, "desc": "감성 가득한 작은 승리의 별!"},
            {"name": "밀로틱", "id": 350, "desc": "아름다움의 극치, 예술 그 자체!"},
            {"name": "라티오스", "id": 381, "desc": "자유롭게 하늘을 나는 감성가!"},
        ]
    },
    "ESTP": {
        "personality": "대담한 사업가 🎲",
        "color": "#7C3AED",
        "pokemons": [
            {"name": "팬텀", "id": 94, "desc": "장난기 가득한 분위기 메이커!"},
            {"name": "리오르", "id": 447, "desc": "도전을 즐기는 열혈 파이터!"},
            {"name": "한카리아스", "id": 445, "desc": "거침없이 돌진하는 행동파!"},
            {"name": "루챠불", "id": 701, "desc": "화려한 기술의 프로레슬러!"},
            {"name": "번치코", "id": 257, "desc": "불꽃처럼 뜨거운 액션 히어로!"},
        ]
    },
    "ESFP": {
        "personality": "자유로운 연예인 🌟",
        "color": "#FB923C",
        "pokemons": [
            {"name": "부스터", "id": 136, "desc": "정열적으로 빛나는 스타!"},
            {"name": "쥬피썬더", "id": 135, "desc": "짜릿한 매력의 인기쟁이!"},
            {"name": "메로엣타", "id": 648, "desc": "노래와 춤의 디바!"},
            {"name": "치라치노", "id": 573, "desc": "반짝반짝 화려한 매력!"},
            {"name": "님피아", "id": 700, "desc": "사랑스러움의 끝판왕!"},
        ]
    },
}

# 포켓몬 이미지 URL 생성 함수
def get_pokemon_image(pokemon_id):
    return f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon_id}.png"

# 커스텀 CSS
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 3em;
        background: linear-gradient(90deg, #FF6B6B, #FFD93D, #6BCB77, #4D96FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        padding: 20px;
    }
    .sub-title {
        text-align: center;
        color: #666;
        font-size: 1.2em;
        margin-bottom: 30px;
    }
    .pokemon-card {
        background: linear-gradient(135deg, #FFF5E1, #FFE0F0);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        margin: 20px 0;
    }
    .mini-card {
        background: white;
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    .stButton button {
        background: linear-gradient(90deg, #FF6B6B, #FFD93D);
        color: white;
        font-size: 1.2em;
        font-weight: bold;
        border: none;
        border-radius: 25px;
        padding: 10px 30px;
        width: 100%;
    }
    .stButton button:hover {
        transform: scale(1.05);
        transition: 0.3s;
    }
</style>
""", unsafe_allow_html=True)

# 타이틀
st.markdown('<h1 class="main-title">⚡ MBTI 포켓몬 추천기 ⚡</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">너에게 딱 맞는 포켓몬 파트너들을 찾아줄게! 🎈</p>', unsafe_allow_html=True)

st.markdown("---")

# MBTI 선택
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🧩 너의 MBTI를 알려줘!")
    mbti_list = list(mbti_pokemon.keys())
    selected_mbti = st.selectbox(
        "MBTI 선택",
        mbti_list,
        index=0,
        label_visibility="collapsed"
    )

with col2:
    st.markdown("### 🎯 또는 직접 선택해봐!")
    e_i = st.radio("에너지", ["E (외향)", "I (내향)"], horizontal=True)
    n_s = st.radio("인식", ["N (직관)", "S (감각)"], horizontal=True)
    t_f = st.radio("판단", ["T (사고)", "F (감정)"], horizontal=True)
    j_p = st.radio("생활", ["J (계획)", "P (탐색)"], horizontal=True)
    
    custom_mbti = e_i[0] + n_s[0] + t_f[0] + j_p[0]
    st.info(f"🎨 선택한 MBTI: **{custom_mbti}**")

st.markdown("---")

use_custom = st.checkbox("✨ 직접 선택한 MBTI 사용하기")
final_mbti = custom_mbti if use_custom else selected_mbti

# 추천 모드 선택
mode = st.radio(
    "🎮 추천 모드를 선택해줘!",
    ["🎁 베스트 매치 (모든 포켓몬 보기)", "🎲 랜덤 뽑기 (한 마리만!)"],
    horizontal=True
)

# 결과 보기 버튼
if st.button("🎉 나의 포켓몬 파트너 보기! 🎉"):
    data = mbti_pokemon[final_mbti]
    
    st.balloons()
    
    st.markdown(f"""
    <div class="pokemon-card" style="border: 3px solid {data['color']};">
        <h2 style="color: {data['color']};">✨ {final_mbti}의 포켓몬 파트너 ✨</h2>
        <h3>{data['personality']}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    if "랜덤" in mode:
        # 랜덤 한 마리
        chosen = random.choice(data['pokemons'])
        
        st.markdown(f"<h2 style='text-align:center; color:{data['color']};'>🎊 {chosen['name']} 🎊</h2>", unsafe_allow_html=True)
        
        col_a, col_b, col_c = st.columns([1, 2, 1])
        with col_b:
            st.image(get_pokemon_image(chosen['id']), use_container_width=True)
        
        st.success(f"💌 **{chosen['desc']}**")
        
        # 케미 게이지
        chemi = random.randint(85, 99)
        st.markdown("### 🌟 너와의 케미는?")
        st.progress(chemi)
        st.caption(f"✨ {chemi}% 일치! 운명의 파트너예요! ✨")
        
        st.info("💡 다시 버튼을 누르면 다른 포켓몬이 나올 수 있어요!")
    
    else:
        # 전체 보기
        st.markdown("### 🌟 너와 어울리는 포켓몬 TOP 5!")
        
        for i, pokemon in enumerate(data['pokemons']):
            with st.container():
                col_img, col_info = st.columns([1, 2])
                
                with col_img:
                    st.image(get_pokemon_image(pokemon['id']), width=150)
                
                with col_info:
                    medal = ["🥇", "🥈", "🥉", "🏅", "🏅"][i]
                    st.markdown(f"#### {medal} {pokemon['name']}")
                    st.write(f"💬 {pokemon['desc']}")
                    chemi = random.randint(80, 99)
                    st.progress(chemi)
                    st.caption(f"케미 지수: {chemi}%")
                
                st.markdown("---")

st.markdown(
    '<p style="text-align:center; color:#999;">Made with 💖 for 당곡고 학생들 | Powered by Streamlit</p>',
    unsafe_allow_html=True
)
