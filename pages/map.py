import streamlit as st
import pandas as pd
import pydeck as pdk

# 데이터 로드
data1 = pd.read_csv("국어.csv")
data2 = pd.read_csv("수학.csv")
data3 = pd.read_csv("영어.csv")

# 색상 매핑
colors = {
    '화법과 작문': [255, 165, 0, 160],
    '언어와 매체': [0, 128, 0, 160],
    '미선택': [128, 0, 128, 160],
    '확률과 통계': [255, 20, 147, 160],
    '미적분': [0, 191, 255, 160],
    '기하': [255, 69, 0, 160],
    '선택함': [218, 112, 214, 160]
}

# 과목별 선택과목 순서
subject_order = {
    '국어': ['화법과 작문', '언어와 매체', '미선택'],
    '수학': ['확률과 통계', '미적분', '기하', '미선택'],
    '영어': ['선택함', '미선택']
}

# 지도 생성 함수
def create_map(data, subject, color):
    filtered_data = data[data['선택과목'] == subject].copy()
    filtered_data['color'] = [color] * len(filtered_data)
    filtered_data['radius'] = filtered_data['지원자수']*0.8 # 지원자 수에 따라 원의 크기 조절
    layer = pdk.Layer(
        'ScatterplotLayer',
        filtered_data,
        get_position=['longitude', 'latitude'],
        get_color='color',
        get_radius='radius',
        pickable=True,
        opacity=0.8
    )
    view_state = pdk.ViewState(
        latitude=filtered_data['latitude'].mean(),
        longitude=filtered_data['longitude'].mean(),
        zoom=6
    )
    return pdk.Deck(layers=[layer], initial_view_state=view_state)

tab1, tab2, tab3 = st.tabs(['국어', '수학', '영어'])

with tab1:
    st.header('국어 영역별 지원자 수')
    for subject in subject_order['국어']:
        st.subheader(subject)
        st.pydeck_chart(create_map(data1, subject, colors[subject]))

with tab2:
    st.header('수학 영역별 지원자 수')
    for subject in subject_order['수학']:
        st.subheader(subject)
        st.pydeck_chart(create_map(data2, subject, colors[subject]))

with tab3:
    st.header('영어 영역별 지원자 수')
    for subject in subject_order['영어']:
        st.subheader(subject)
        st.pydeck_chart(create_map(data3, subject, colors[subject]))