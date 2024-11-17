import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

# 데이터 로드
data = pd.read_csv("탐구.csv")

# Session State 설정
if "ID" not in st.session_state:
    st.session_state["ID"] = "None"
ID = st.session_state["ID"]

# 폰트 경로 설정
font_dir = os.path.join(os.path.dirname(__file__), "fonts")
font_path = os.path.join(font_dir, "나눔고딕 보통.ttf")

try:
    font_prop = fm.FontProperties(fname=font_path)
    plt.rcParams['font.family'] = font_prop.get_name()
    plt.rcParams['axes.unicode_minus'] = False
except Exception as e:
    st.error(f"폰트 설정 중 오류 발생: {e}")

with st.sidebar:
    st.caption(f'{ID}님 접속중')

with st.form("input"):
    exploration = st.multiselect("탐구영역", data['탐구영역'].unique())
    submitted = st.form_submit_button("조회")
    
    if submitted and exploration:
        filtered_data = data[data['탐구영역'].isin(exploration)]
        if not filtered_data.empty:
            fig, ax = plt.subplots()
            ax.bar(filtered_data['선택과목'], filtered_data['인원수'], color='green')
            ax.set_xlabel('선택과목')
            ax.set_ylabel('인원 수')
            ax.set_title('선택과목별 인원 수')
            ax.set_xticks(range(len(filtered_data['선택과목'])))
            ax.set_xticklabels(filtered_data['선택과목'], rotation=45, ha="right")
            st.pyplot(fig)
        else:
            st.error("선택한 탐구영역에 대한 데이터가 없습니다.")