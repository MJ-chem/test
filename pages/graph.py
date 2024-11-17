import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("탐구.csv")

if "ID" not in st.session_state:
    st.session_state["ID"] = "None"

ID = st.session_state["ID"]

with st.sidebar:
    st.caption(f'{ID}님 접속중')

# Matplotlib 기본 폰트 변경 (웹 안전 폰트 사용)
plt.rcParams['font.family'] = 'Arial'  # 웹 안전 폰트
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 오류 방지

with st.form("input"):
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
            st.error("선택한 탐구영역에 대한 데이터가 없습니다.")