import streamlit as st
import pandas as pd
import time



st.title("대학수학능력시험 응시현황")
st.image('image.jpeg')
data = pd.read_csv("members.csv") # 회원 목록 불러오는 코드
data["PW"] = data["PW"].astype(str)
data

with st.form("login_form"): # 들여쓰기는 선택하고 Tab
    ID = st.text_input("ID", placeholder="아이디를 입력하세요") # placeholder (안내문구)
    PW = st.text_input("Password", type="password", placeholder="비밀번호를 입력하세요") # type (비밀)
    submit_button = st.form_submit_button("로그인") # 회원 목록(ID PW)이 있어야 함. csv(utf-8) 형태

if submit_button:
    if not ID or not PW:
        st.warning("ID와 비밀번호를 모두 입력해주세요.")
    else:
        # 사용자 확인
        user = data[(data["ID"] == ID) & (data["PW"] == str(PW))] # PW 숫자형 아니므로 문자형으로 (위에서 설정했으니까 그냥 PW라고 입력해도 되는 듯)
        
        if not user.empty:
            st.success(f"{ID}님 환영합니다!")
            st.session_state["ID"]=ID # 변수 딕셔너리에 저장하는 방법
            
            progress_text = "로그인 중입니다.잠시만 기다려주세요"
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text=progress_text)
            time.sleep(1)
            my_bar.empty()
            st.switch_page("pages/graph.py") # 같은 폴더에 pages 폴더 생성
            
            
        else:
            st.error("아이디 또는 비밀번호가 일치하지 않습니다.")
            # st.warning('사용자 정보가 일치하지 않습니다.')