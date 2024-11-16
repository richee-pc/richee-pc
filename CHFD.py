import streamlit as st
from datetime import datetime
import random

# 접속자 수 저장 변수
if "visitor_count" not in st.session_state:
    st.session_state["visitor_count"] = random.randint(50, 150)  # 기본 접속자 수 (랜덤)

# 접속자 증가
st.session_state["visitor_count"] += 1

# 웹 페이지 설정
st.set_page_config(
    page_title="조선대학교부속고등학교 급식메뉴",
    page_icon="🍱",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 스타일 적용
st.markdown(
    """
    <style>
        body {
            font-family: 'Noto Sans KR', sans-serif;
            background-color: #e3f2fd;
        }
        .title-container {
            text-align: center;
            padding: 10px;
            background-color: #1a73e8;
            border-radius: 10px;
            color: white;
            box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
        }
        .menu-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
            gap: 20px;
            margin-top: 20px;
        }
        .menu-card {
            width: 300px;
            background: white;
            border-radius: 15px;
            box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
            padding: 20px;
            text-align: center;
        }
        .menu-title {
            font-size: 1.5em;
            color: #1a73e8;
            border-bottom: 2px solid #1a73e8;
            margin-bottom: 15px;
            padding-bottom: 5px;
        }
        .menu-list {
            list-style: none;
            padding: 0;
        }
        .menu-item {
            padding: 8px 0;
            border-bottom: 1px solid #f0f0f0;
            transition: background-color 0.3s;
        }
        .menu-item:hover {
            background-color: #f0f8ff;
        }
        .footer {
            text-align: center;
            margin-top: 30px;
            color: #666;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# 타이틀 표시
st.markdown(
    """
    <div class="title-container">
        <h1>🍱 조선대학교부속고등학교 급식메뉴 🍱</h1>
    </div>
    """,
    unsafe_allow_html=True,
)

# 현재 날짜 표시
current_date = datetime.now().strftime("%Y년 %m월 %d일 (%A)")
st.markdown(f"<div style='text-align: center; color: #555; margin-top: 20px;'>오늘은 {current_date}입니다.</div>", unsafe_allow_html=True)

# 급식 메뉴 데이터
lunch_menu = ["백미밥", "소고기미역국", "돈육불고기", "배추김치", "깍두기", "요구르트"]
dinner_menu = ["잡곡밥", "된장찌개", "고등어구이", "무나물", "총각김치", "바나나"]

# 메뉴 카드 렌더링
st.markdown('<div class="menu-container">', unsafe_allow_html=True)

for title, menu in [("🍱 점심 메뉴", lunch_menu), ("🌙 저녁 메뉴", dinner_menu)]:
    st.markdown(
        f"""
        <div class="menu-card">
            <div class="menu-title">{title}</div>
            <ul class="menu-list">
                {''.join([f"<li class='menu-item'>{item}</li>" for item in menu])}
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("</div>", unsafe_allow_html=True)

# 접속자 수 표시
st.markdown(
    f"""
    <div class="footer">
        <p>🧑‍🤝‍🧑 현재 접속자 수: <strong>{st.session_state['visitor_count']}명</strong></p>
    </div>
    """,
    unsafe_allow_html=True,
)
