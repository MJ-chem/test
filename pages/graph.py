import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("탐구.csv")

if "ID" not in st.session_state:
    st.session_state["ID"] = "None"

ID = st.session_state["ID"]

with st.sidebar:
    st.caption(f'{ID}님 접속중')

# CSS 스타일 추가
st.markdown(
    """
    <style>
        .title {
            font-family: 'Noto Sans KR', sans-serif;
            font-size: 24px;
            font-weight: bold;
            color: #2b2b2b;
            text-align: center;
            margin-bottom: 20px;
        }
        .subtitle {
            font-family: 'Noto Sans KR', sans-serif;
            font-size: 18px;
            color: #3a3a3a;
            text-align: left;
            margin-bottom: 15px;
        }
        .error-message {
            font-family: 'Noto Sans KR', sans-serif;
            color: red;
            font-size: 16px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 제목 표시
st.markdown('<div class="title">탐구영역 선택과목별 인원 수</div>', unsafe_allow_html=True)

# Matplotlib 기본 폰트 변경 (웹 안전 폰트 - Noto Sans CJK 사용)
plt.rcParams['font.family'] = 'Noto Sans CJK JP'  # Noto Sans CJK 설정
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 오류 방지

# 입력 폼 생성
with st.form("input"):
    st.markdown('<div class="subtitle">탐구영역을 선택하세요:</div>', unsafe_allow_html=True)
    exploration = st.multiselect("탐구영역", data['탐구영역'].unique())
    submitted = st.form_submit_button("조회")
    
    if submitted and exploration:
        # 사용자가 선택한 탐구영역에 대한 데이터 필터링
        filtered_data = data[data['탐구영역'].isin(exploration)]
        
        if not filtered_data.empty:
            # 인원 수를 직접 사용하여 막대 그래프 생성
            fig, ax = plt.subplots()
            ax.bar(filtered_data['선택과목'], filtered_data['인원수'], color='green')  # 색상 지정
            ax.set_xlabel('선택과목')
            ax.set_ylabel('인원 수')
            ax.set_title('선택과목별 인원 수')
            # x축 레이블 간격 조정
            ax.set_xticks(range(len(filtered_data['선택과목'])))
            ax.set_xticklabels(filtered_data['선택과목'], rotation=45, ha="right")  # 회전하여 레이블 표시
            st.pyplot(fig)
        else:
            st.markdown('<div class="error-message">선택한 탐구영역에 대한 데이터가 없습니다.</div>', unsafe_allow_html=True)