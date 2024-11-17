import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

# 현재 디렉토리와 폰트 경로 설정
current_dir = os.path.dirname(__file__)
font_path = os.path.join(current_dir, "fonts", "나눔고딕 보통.TTF")
data_path = os.path.join(current_dir, "..", "탐구.csv")

# 폰트 설정
if not os.path.exists(font_path):
    st.error(f"폰트 파일을 찾을 수 없습니다: {font_path}")
else:
    font_prop = fm.FontProperties(fname=font_path)

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
        # 선택한 탐구영역 데이터 필터링
        filtered_data = data[data['탐구영역'].isin(exploration)]
        
        if not filtered_data.empty:
            # 그래프 생성 시 폰트 직접 지정
            fig, ax = plt.subplots()
            ax.bar(filtered_data['선택과목'], filtered_data['인원수'], color='green')
            ax.set_xlabel('선택과목', fontproperties=font_prop)
            ax.set_ylabel('인원 수', fontproperties=font_prop)
            ax.set_title('선택과목별 인원 수', fontproperties=font_prop)
            ax.set_xticks(range(len(filtered_data['선택과목'])))
            ax.set_xticklabels(
                filtered_data['선택과목'], 
                rotation=45, 
                ha="right", 
                fontproperties=font_prop
            )
            st.pyplot(fig)
        else:
            st.error("선택한 탐구영역에 대한 데이터가 없습니다.")