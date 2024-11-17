import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

# 파일 경로 설정
current_dir = os.path.dirname(__file__)  # 현재 파일의 디렉토리
font_path = os.path.join(current_dir, "fonts", "나눔고딕 보통.ttf")  # 폰트 경로
data_path = os.path.join(current_dir, "..", "탐구.csv")  # 데이터 경로 (루트 디렉토리)

# 폰트 설정
if not os.path.exists(font_path):
    st.error(f"폰트 파일을 찾을 수 없습니다: {font_path}")
else:
    font_prop = fm.FontProperties(fname=font_path)
    plt.rcParams['font.family'] = font_prop.get_name()
    plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 오류 방지

# 데이터 로드
if not os.path.exists(data_path):
    st.error(f"데이터 파일을 찾을 수 없습니다: {data_path}")
else:
    data = pd.read_csv(data_path)

if "ID" not in st.session_state:
    st.session_state["ID"] = "None"

ID = st.session_state["ID"]

with st.sidebar:
    st.caption(f'{ID}님 접속 중')

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
