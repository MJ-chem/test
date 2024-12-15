import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os
from PIL import Image

# 페이지 설정
st.set_page_config(
    page_title="중화 반응 앱",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 사이드바 HTML 스타일 적용
st.sidebar.markdown("""
    <div style="background-color:#000033; padding:20px; border-radius:10px;">
        <h2 style="color:white; font-weight:bold; font-size:24px; text-align:center;">
            ☆ Navigation ☆
        </h2>
    </div>
""", unsafe_allow_html=True)

menu = {
    "🏠 Home": "🏠 Home",
    "📘 개념 이해": "📘 개념 이해",
    "🔬 실험 수행": "🔬 실험 수행",
    "🌍 실생활 적용": "🌍 실생활 적용",
    "💬 의견 나누기": "💬 의견 나누기"
}

selected_page = st.sidebar.radio(
    label="",
    options=list(menu.keys()),
    format_func=lambda x: menu[x]
)

# 페이지 내용 출력
if selected_page == "🏠 Home":
    st.image("1.jpg", width=600)
    st.header('🌟 중화 반응 :blue[알고 보면 쉽다~!]', divider="rainbow")
    st.markdown("""
    <div style="text-align: right; font-size:35px; font-weight: bold; color: black;">
        가보자고~!! 🌟
    </div>
    """, unsafe_allow_html=True)
    st.divider()

elif selected_page == "📘 개념 이해":
    st.title("📘 중화 반응 개념 복습하기")
    st.divider()

    # 한글 폰트 설정 (한글 깨짐 방지)
    matplotlib.rc("font", family="NanumGothic")
    plt.rcParams["axes.unicode_minus"] = False  # 마이너스 기호 깨짐 방지

    # 앱 시작
    with st.expander("", expanded=True):
        st.header("✔️ 중화 반응을 모형으로 설명하기")
        st.markdown("""
        <div style='background-color: #eae2fc; padding: 20px; border-radius: 10px; font-size: 25px;'>
            그림은 0.1M HCl(aq) 200mL가 0.2M NaOH(aq) 100mL와 반응할 때, 각 용액 속에 존재하는 이온들을 입자 모형으로 나타낸 것이다.<br>
            각 용액에 존재하는 이온들의 입자 모형을 참고하여 0.1M HCl(aq) 200mL가 들어 있는 비커에 <br> 
            0.2M NaOH(aq)을 50mL씩 첨가할 때, 혼합 용액 속에 존재하는 각 이온의 수를 아래(⬇️) 표에 입력하세요~! <br>
            (단, 용액 속에 존재하는 각 이온의 수는 입자 모형의 수와 같다.)
        </div><br><br>
        """, unsafe_allow_html=True)
        st.image("2.jpg", width=800)    

        st.divider()
    
        # 데이터 입력 창을 틀 안에 배치    
        st.subheader("⚫ 데이터 입력")
        num_rows = st.number_input("입력할 데이터 행의 개수", min_value=1, max_value=10, value=5)

        data = {
            "NaOH 부피 (mL)": [],
            "H⁺": [],
            "Cl⁻": [],
            "Na⁺": [],
            "OH⁻": []
        }

        for i in range(num_rows):
            st.markdown(f"#### 데이터 행 {i+1}")
            cols = st.columns(5)

            vol = cols[0].number_input(f"0.2M NaOH(aq) 부피 (mL)", min_value=0, value=0, step=10, key=f"vol_{i}")
            h_ion = cols[1].number_input(f"H⁺", min_value=0, value=0, key=f"h_ion_{i}")
            cl_ion = cols[2].number_input(f"Cl⁻", min_value=0, value=0, key=f"cl_ion_{i}")
            na_ion = cols[3].number_input(f"Na⁺", min_value=0, value=0, key=f"na_ion_{i}")
            oh_ion = cols[4].number_input(f"OH⁻", min_value=0, value=0, key=f"oh_ion_{i}")

            data["NaOH 부피 (mL)"].append(vol)
            data["H⁺"].append(h_ion)
            data["Cl⁻"].append(cl_ion)
            data["Na⁺"].append(na_ion)
            data["OH⁻"].append(oh_ion)
        
        st.divider()

        # 데이터프레임 생성 및 출력
        df = pd.DataFrame(data)
        st.subheader("✅ 입력된 데이터")
        st.dataframe(df, width=1000, height=250)

        st.divider()

        # 그래프 시각화    
        st.subheader("⚫ 그래프 시각화")
        graph_type = st.selectbox("그래프 종류를 선택하세요", ["꺾은선 그래프", "막대 그래프", "원 그래프"])

        if graph_type == "꺾은선 그래프":
            with st.container():
                plt.figure(figsize=(5, 3))
                for column in df.columns[1:]:
                    plt.plot(df["NaOH 부피 (mL)"], df[column], marker="o", label=column.replace("⁺", "$^{+}$").replace("⁻", "$^{-}$"))
                plt.xlabel("NaOH 부피 (mL)")
                plt.ylabel("이온 수")
                plt.title("NaOH 부피에 따른 이온 수 변화")
                plt.legend()
                st.pyplot(plt)

        elif graph_type == "막대 그래프":
            with st.container():
                plt.figure(figsize=(5, 3))
                for column in df.columns[1:]:
                    plt.bar(df["NaOH 부피 (mL)"], df[column], label=column.replace("⁺", "$^{+}$").replace("⁻", "$^{-}$"), alpha=0.7)
                plt.xlabel("NaOH 부피 (mL)")
                plt.ylabel("이온 수")
                plt.title("NaOH 부피에 따른 이온 수 변화")
                plt.legend()
                st.pyplot(plt)

        elif graph_type == "원 그래프":
            with st.container():
                row_index = st.slider("원 그래프로 볼 행 선택 (0부터 시작)", min_value=0, max_value=num_rows - 1, value=0)
                row_data = df.iloc[row_index, 1:].fillna(0)

                if row_data.sum() == 0:
                    st.error("선택된 행의 데이터 합이 0이므로 원 그래프를 표시할 수 없습니다.")
                else:
                    plt.figure(figsize=(6, 6))
                    labels = [label.replace("⁺", "$^{+}$").replace("⁻", "$^{-}$") for label in row_data.index]
                    plt.pie(row_data, labels=labels, autopct="%.1f%%", startangle=140)
                    plt.title(f"NaOH 부피 {df.iloc[row_index, 0]} mL에서의 이온 비율")
                    st.pyplot(plt)

if "submitted" not in st.session_state:
    st.session_state["submitted"] = False
if "checked_answers" not in st.session_state:
    st.session_state["checked_answers"] = False

elif selected_page == "🔬 실험 수행":
    # 페이지 제목
    st.title("🔬 실험 수행하기")
    st.divider()

    st.header("✔️ 실험을 설계하고 수행하여 미지 시료 농도를 알아내보자~!")
    st.image("3.jpg", width=300)
    st.divider()

    # 질문에 대한 답변 작성 섹션
    with st.expander("", expanded=True):
        st.markdown("""
        <div style='background-color: #e2f4fc; padding: 20px; border-radius: 10px; font-size: 25px; color: navy;'>
            <b>Q. 어느날 실험실에서 농도가 표시되지 않은 염산병을 발견했어. 이 염산의 농도를 알아내려면 어떻게 해야 할까?</b><br>
        </div><br><br>
        """, unsafe_allow_html=True)
        st.subheader("➡️ 위 질문에 대한 답변을 작성해 보세요:")
        st.write("📌 답변을 작성해야 다음 활동으로 연결됩니다~!")
        # 학생 입력 칸 생성
        student_input = st.text_area(
            "",
            placeholder="힌트: 중화 반응의 양적 관계를 이용하여 미지 농도의 산 또는 염기의 농도를 알아내는 방법",
            height=100
        )

        # 제출 버튼
        if st.button("제출하기", key="submit_button"):
            if student_input.strip():
                st.success("작성 완료~! 다음 활동으로 연결됩니다/ 아래로 스크롤을 내려보세요~! Go Go!")
                st.write(f"**입력한 내용:** {student_input}")
                st.session_state["submitted"] = True
            else:
                st.warning("내용을 입력해야 제출 가능합니다~!")

    if st.session_state["submitted"]:  # 답변 제출 완료 후에만 실행        
        with st.expander("", expanded=True):
            st.title("✔️ 중화 적정에 사용되는 실험도구 찾기")
            st.subheader("➡️ 아래 제시된 실험기구 사진을 보고, 이름과 기능을 입력하세요.")

            # 실험기구 목록 (정답 데이터)
            equipment = {
                "피펫": {
                    "image": "4.jpg",
                    "function": "액체의 부피를 정확히 취하여 옮길 때 사용",
                },
                "뷰렛": {
                    "image": "5.jpg",
                    "function": "가해지는 표준 용액의 부피를 측정할 때 사용",
                },
                "삼각 플라스크": {
                    "image": "6.jpg",
                    "function": "농도를 측정하고자 하는 수용액을 담는 데 사용",
                },
            }

            # 사용자 입력 데이터 저장
            results = {}
            is_successful = True

            # UI 생성 (사진, 이름 입력, 드롭다운을 한 줄에 배치)
            columns = st.columns(3)  # 세 개의 열 생성
            for idx, (correct_name, data) in enumerate(equipment.items()):
                with columns[idx]:  # 각 열에 요소 추가
                    # 이미지 표시 (캡션 제거 또는 힌트 제공)
                    st.image(data["image"], width=150)  # 캡션 제거
                    
                    # 이름 입력
                    user_name = st.text_input(f"이 실험기구의 이름을 입력하세요:", key=f"name_{correct_name}")
                    
                    # 드롭다운 메뉴
                    user_function = st.selectbox(
                        f"기능 선택:",
                        ["--기능 선택--", "액체의 부피를 정확히 취하여 옮길 때 사용", "농도를 측정하고자 하는 수용액을 담는 데 사용", "가해지는 표준 용액의 부피를 측정할 때 사용"],
                        key=f"function_{correct_name}",
                    )
                    results[correct_name] = {"입력된 이름": user_name, "선택된 기능": user_function}

                    # 정답 확인
                    if user_name != correct_name or user_function != data["function"]:
                        is_successful = False

            # 결과 확인 버튼
            if st.button("정답 확인", key="check_answers"):
                st.session_state["checked_answers"] = True
                if is_successful:
                    st.success("🎉 중화 적정에 사용되는 실험 기구에 대해 잘 알고 있네요~! 이제 실험을 진행해 봅시다!")
                else:
                    st.error("❌ 이대로 포기하기는 이르다~! 한번 더 시도해 보세요.")
            
        with st.expander("", expanded=True):
            st.title("🟢 중화 적정 실험 과정")
            # 다단 레이아웃 생성 (2단)
            col1, col2 = st.columns([1, 4])  # 왼쪽과 오른쪽의 비율 설정 (1:1 비율)

            # 왼쪽: 실험 장치 사진
            with col1:
                st.header("🧪 그림 1. 실험 장치")
                # 실험 장치 사진 추가
                image = Image.open("11.jpg")
                st.image(image, use_container_width=True)  # 이미지와 캡션

            # 오른쪽: 실험 과정 설명
            with col2:
                st.header("📄 실험 과정")
                # 실험 과정 작성
                st.markdown("""
                <div style="font-size: 30px; font-weight: bold; line-height: 2.0; margin-left: 30px;">
                    1. 그림 1과 같이 실험 장치를 준비한다.<br>
                    2. 삼각 플라스크에 교반 자석을 넣고, 피펫으로 미지 농도의 HCl(aq) 20mL를 넣는다.<br>
                    3. 과정 2의 삼각 플라스크에 페놀프탈레인 용액을 2~3방울 떨어뜨린다.<br>
                    4. 깔때기를 이용하여 0.1M NaOH(aq)을 뷰렛에 넣는다.<br>
                    5. 뷰렛 아래에 빈 용기를 댄 다음 뷰렛의 꼭지를 열어 꼭지 아래에도 NaOH(aq)을 채운 후 꼭지를 잠근다.<br>
                    6. 뷰렛의 눈금을 읽어 NaOH(aq)의 처음 부피를 기록한다.<br>
                    7. HCl(aq)이 들어 있는 삼각 플라스크를 교반기 위에 올려놓고 교반기를 작동한 후, <span style="text-indent: 30px; display: inline-block;">NaOH(aq)을 천천히 떨어뜨린다.<br>
                    8. 수용액이 붉은색으로 변하기 시작하면, 꼭지를 조절하여 소량씩 떨어뜨린다.<br>
                    9. 삼각 플라스크에 들어 있는 용액 전체가 붉은색으로 변하는 순간 꼭지를 잠근다.<br>
                    10. NaOH(aq)의 나중 부피를 측정하여 기록한다.
                </div>
                """, unsafe_allow_html=True)
            st.divider()

            st.title("✔️ 중화 적정 실험 결과 기록하기")
            
            # 초기 데이터프레임 생성
            data = {
                "뷰렛의 처음 눈금 (mL)": [0.0],
                "뷰렛의 나중 눈금 (mL)": [0.0],
                "소모된 0.1 M NaOH의 부피 (mL)": [0.0],  # 자동 계산 결과
            }

            df = pd.DataFrame(data)

            # 제목
            st.subheader("📊 측정한 데이터 입력")
            st.markdown("➡️ 아래 제시된 표에 실험 과정 6과 10에서 측정한 NaOH(aq)의 부피를 입력하세요. 뷰렛의 처음 눈금과 나중 눈금을 입력하면, 소모된 NaOH(aq)의 부피가 자동으로 계산됩니다.")

            # 입력 필드 생성
            initial = st.number_input("뷰렛의 처음 눈금 (mL)", min_value=0.0, step=0.1, value=0.0)
            final = st.number_input("뷰렛의 나중 눈금 (mL)", min_value=0.0, step=0.1, value=0.0)

            # 계산
            if final <= initial:
                volume = initial - final
                st.markdown(f"<div style='font-size: 20px; color: red;'>▶ 소모된 0.1 M NaOH의 부피 = {volume:.2f} mL</div>", unsafe_allow_html=True)
            else:
                st.error("뷰렛의 처음 눈금은 나중 눈금보다 커야 합니다!")

            st.divider()

        with st.expander("", expanded=True):
            # 제목
            st.title("🟢 <참고 자료> 중화 반응의 양적 관계")
            st.image("12.jpg", width=900)
            st.divider()

            # 데이터 입력 섹션
            st.header("✔️ 실험실에서 발견한 염산의 농도 계산하기")
            st.subheader("📝 데이터 입력")

            # 입력 칸을 열로 나눔
            col1, col2, col3, col4, col5 = st.columns(5)

            # 입력 칸 (n, M, V, n', V' 입력)
            with col1:
                n = st.number_input("n (NaOH(aq)의 가수)", min_value=0, step=1)
            with col2:
                M = st.number_input("M (NaOH(aq)의 몰농도)", min_value=0.0, max_value=10.0, step=0.1, format="%.1f")
            with col3:
                V = st.number_input("V (NaOH(aq)의 부피, mL)", min_value=0, step=5)
            with col4:
                n_prime = st.number_input("n' (HCl(aq)의 가수)", min_value=0, step=1)
            with col5:
                V_prime = st.number_input("V' (HCl(aq)의 부피, mL)", min_value=0, step=5)

            # 미지수 M' 계산
            if V_prime > 0:  # 부피 V'가 0이 아닌 경우만 계산
                M_prime = round((n * M * V) / (n_prime * V_prime), 2)  # 소수점 첫째 자리까지 계산
            else:
                M_prime = None

            # 계산 결과 출력
            st.subheader("📊 계산 결과")
            if M_prime is not None:
                st.markdown(
                    f"<div style='font-size: 24px; color: red; font-weight: bold;'>M' = {M_prime:.2f} M</div>",
                    unsafe_allow_html=True,
                )
            else:
                st.error("V'는 0이 될 수 없습니다. 올바른 값을 입력하세요.")

            
elif selected_page == "🌍 실생활 적용":
    # 페이지 제목
    st.title("🌍 해양 산성화의 원인 파악하기")
    st.image("7.jpg", width=1200)
    st.divider()

    with st.expander("", expanded=True):
        st.header("📈🔍 북태평양 하와이 마우나로아산과 하와이 근해 알로하 측정소에서 측정한 대기의 CO\u2082 농도와 해수의 pH")
        
        # 데이터 로드
        file_path = 'data.csv'
        data = pd.read_csv(file_path, encoding='cp949')

        # 데이터 전처리: 공백 제거 및 결측치 처리
        data.columns = data.columns.str.strip()
        data = data.dropna(subset=['마우나로아산 대기 중 CO2 농도(ppm)', '알로하 해수의 pH'], how='all')

        # 드롭다운 메뉴    
        options = ["대기 중 CO\u2082 농도", "알로하 해수의 pH", "전체 보기"]
        selected_option = st.selectbox("✅ 보기 옵션을 선택하세요:", options)
        
        # 선택된 옵션에 따라 그래프 출력
        if selected_option == "대기 중 CO\u2082 농도":
            st.subheader("연도별 대기 중 CO\u2082 농도 변화")
            fig, ax1 = plt.subplots(figsize=(10, 5))
            
            ax1.plot(data['year'], data['마우나로아산 대기 중 CO2 농도(ppm)'], 'r-', label='CO\u2082 농도')
            ax1.set_xlabel('연도')
            ax1.set_ylabel('CO\u2082 농도 (ppm)', color='red')
            ax1.tick_params(axis='y', labelcolor='red')

            plt.legend()
            st.pyplot(fig)

        elif selected_option == "알로하 해수의 pH":
            st.subheader("연도별 해수의 pH 변화")
            fig, ax2 = plt.subplots(figsize=(10, 5))
            
            ax2.plot(data['year'], data['알로하 해수의 pH'], 'b-', label='pH 값')
            ax2.set_xlabel('연도')
            ax2.set_ylabel('pH', color='blue')
            ax2.tick_params(axis='y', labelcolor='blue')

            plt.legend()
            st.pyplot(fig)
        
        elif selected_option == "전체 보기":
            st.subheader("연도별 대기 중 CO\u2082 농도와 해수의 pH 변화")
            
            # CO2 농도와 pH 변화 그래프를 하나의 그래프에 표시
            fig, ax1 = plt.subplots(figsize=(10, 5))

            ax1.plot(data['year'], data['마우나로아산 대기 중 CO2 농도(ppm)'], 'r-', label='CO\u2082 농도')
            ax1.set_xlabel('연도')
            ax1.set_ylabel('CO\u2082 농도 (ppm)', color='red')
            ax1.tick_params(axis='y', labelcolor='red')

            ax2 = ax1.twinx()  # 동일한 x축을 사용하는 두 번째 y축
            ax2.plot(data['year'], data['알로하 해수의 pH'], 'b-', label='pH 값')
            ax2.set_ylabel('pH', color='blue')
            ax2.tick_params(axis='y', labelcolor='blue')

            fig.legend(loc="upper left")
            st.pyplot(fig)

        # 원본 데이터 출력
        st.subheader("원본 데이터")
        st.dataframe(data)
        st.write("출처: NOAA 태평양 해양 환경 연구소")
        st.divider()

        st.markdown("""
            <div style='background-color: #e2f4fc; padding: 20px; border-radius: 10px; font-size: 25px; color: navy;'>
            <b>Q. 마우나로아산 대기 중 CO\u2082 농도(ppm)와 알로하 해수의 pH 사이의 관계를 작성해보자~!</b>
            </div><br><br>
            """, unsafe_allow_html=True)
        st.subheader("➡️ 위 질문에 대한 답변을 작성해 보세요:")

        # 학생 입력 칸 생성
        student_input = st.text_area(
            "", height=150
        )

        # 제출 버튼
        if st.button("제출하기", key="submit_button1"):
            if student_input.strip():
                st.success("작성 완료~! 다음 활동으로 Go Go!")
                st.write(f"**입력한 내용:** {student_input}")
                st.session_state["submitted"] = True
            else:
                st.warning("내용을 입력해야 제출 가능합니다~!")
        
    with st.expander("", expanded=True):    
        st.header("✔️ 해양 산성화에서 시작된 해양 생태계의 변화")
        st.divider()
        st.subheader("🔍 자료1. 해양 산성화가 되는 원리")
        st.image("9.jpg", width=800)
        st.write("출처: 한국해양과학기술원, ISSUE")
        st.divider()

        st.subheader("🔍 자료2. IPCC 4차 보고서에 제시된 이산화탄소 방출 4가지 시나리오에 따른 산성도(pH) 감소 예측치")
        st.image("10.jpg", width=1400)
        st.write("출처: Modified from C. Turley et al.(2010)")
        st.divider()

        st.markdown("""
        <div style='background-color: #e2f4fc; padding: 20px; border-radius: 10px; font-size: 25px; color: navy;'>
            <b>Q. 위에 제시된 자료 1과 자료 2를 토대로 해양 산성화가<br> 
            <span style="text-indent: 30px; display: inline-block;">탄산 칼슘(CaCO\u2083)을 이용해 골격을 형성하는 해양생물에 미치는 영향을 작성해보자~!</b>
        </div><br><br>
        """, unsafe_allow_html=True)
        st.subheader("➡️ 위 질문에 대한 답변을 작성해 보세요:")

        # 학생 입력 칸 생성
        student_input = st.text_area(
            "",
            placeholder="힌트: 바다 속 OO이온의 감소",
            height=150
        )

        # 제출 버튼
        if st.button("제출하기", key="submit_button2"):
            if student_input.strip():
                st.success("작성 완료~! 다음 활동으로 Go Go!")
                st.write(f"**입력한 내용:** {student_input}")
                st.session_state["submitted"] = True
            else:
                st.warning("내용을 입력해야 제출 가능합니다~!")
            
elif selected_page == "💬 의견 나누기":
    # 페이지 제목
    st.title("💬 지속가능한 환경을 위한 나의 탄소 중립 실천 방안은 무엇인가요?")
    st.image("8.jpg", width=900)
    st.subheader("➡️ 참고 사이트")
    st.write("1. 기후행동 1.5℃: https://c-action.kr/web/index.html")
    st.write("2. 4월 22일 지구의 날 소등 행사: https://blog.naver.com/nie_korea/223420828319")
    st.write("3. 소등 행사로 인한 온실 가스 감축 효과: https://greenium.kr/news/19770/")
    st.write("4. 세계 최대 비영리 자연보전기관 WWF: https://www.wwfkorea.or.kr/")
    st.divider()

    # 파일 경로
    file_path = "ideas.csv"

    # CSV 파일 초기화
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=["학생 이름", "실천 방안", "댓글"])
        df.to_csv(file_path, index=False, encoding="utf-8-sig")

    # 페이지 제목
    st.title("💡 탄소 중립 실천 방안 공유하기")
    st.write("")

    # 학생 아이디어 제출 섹션
    st.subheader("😊여기에 자신의 탄소 중립 실천 방안을 제출하고, 다른 친구들의 의견에도 댓글을 달아주세요~!")
    with st.form("실천 방안 제출"):
        student_name = st.text_input("이름을 입력하세요")
        student_idea = st.text_area("실천 방안을 작성하세요", placeholder="여기에 탄소 중립 실천 방안을 입력하세요...")
        submit_button = st.form_submit_button("제출하기")
        
        if submit_button:
            if student_name.strip() and student_idea.strip():
                # 기존 데이터 불러오기
                df = pd.read_csv(file_path, encoding="utf-8-sig")
                # 새로운 데이터 추가
                new_data = {"학생 이름": student_name, "실천 방안": student_idea, "댓글": ""}
                new_data = pd.DataFrame([new_data])  # 새로운 데이터를 DataFrame으로 변환
                df = pd.concat([df, new_data], ignore_index=True)  # 기존 데이터프레임과 병합
                df.to_csv(file_path, index=False, encoding="utf-8-sig")
                st.success("실천 방안이 성공적으로 제출되었습니다!")
            else:
                st.error("이름과 실천 방안을 모두 입력해야 합니다.")

    st.divider()

    # 제출된 아이디어 공유 섹션
    st.subheader("제출된 실천 방안")
    df = pd.read_csv(file_path, encoding="utf-8-sig")
    for idx, row in df.iterrows():
        with st.expander(f"{row['학생 이름']}님의 실천 방안"):
            st.write(row["실천 방안"])
            st.markdown("**댓글**")
            st.write(row["댓글"] if row["댓글"] else "아직 댓글이 없습니다.")
            
            # 댓글 작성
            comment = st.text_area(f"댓글 작성 ({row['학생 이름']}님의 실천 방안)", key=f"comment_{idx}")
            if st.button(f"댓글 저장 ({idx})", key=f"save_comment_{idx}"):
                if comment.strip():
                    df.loc[idx, "댓글"] = comment
                    df.to_csv(file_path, index=False, encoding="utf-8-sig")
                    st.success("댓글이 저장되었습니다!")
                else:
                    st.error("댓글을 입력해야 합니다.")

