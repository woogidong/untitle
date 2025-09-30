import streamlit as st

import pandas as pd
import numpy as np
import altair as alt

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# ----------------------
# 성적 데이터 시각화 앱
# ----------------------
st.header("성적 데이터 시각화 앱")

# 1. CSV 파일 업로드
uploaded_file = st.file_uploader("성적 데이터 CSV 파일을 업로드하세요", type=["csv"])
df = None
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("데이터 미리보기:")
    st.dataframe(df)
else:
    st.info("CSV 파일을 업로드하면 시각화 옵션이 활성화됩니다.")

# 2. 시각화 옵션
if df is not None:
    st.subheader("시각화 옵션을 선택하세요")
    chart_type = st.radio(
        "그래프 종류",
        ("히스토그램", "막대그래프", "산점도", "상자그림")
    )

    # 3. 변수 선택 및 맞춤형 그래프
    if chart_type == "히스토그램":
        num_cols = df.select_dtypes(include=np.number).columns.tolist()
        if num_cols:
            col = st.selectbox("히스토그램으로 볼 변수를 선택하세요", num_cols)
            st.write(f"### {col}의 히스토그램")
            chart = alt.Chart(df).mark_bar().encode(
                alt.X(col, bin=alt.Bin(maxbins=30)),
                y='count()'
            )
            st.altair_chart(chart, use_container_width=True)
        else:
            st.warning("수치형 변수가 없습니다.")

    elif chart_type == "막대그래프":
        cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
        num_cols = df.select_dtypes(include=np.number).columns.tolist()
        if cat_cols and num_cols:
            cat_col = st.selectbox("범주형(막대) 변수 선택", cat_cols)
            num_col = st.selectbox("수치형(값) 변수 선택", num_cols)
            st.write(f"### {cat_col}별 {num_col}의 막대그래프")
            chart = alt.Chart(df).mark_bar().encode(
                x=cat_col,
                y=alt.Y(num_col, aggregate='mean'),
                tooltip=[cat_col, num_col]
            )
            st.altair_chart(chart, use_container_width=True)
        else:
            st.warning("범주형 또는 수치형 변수가 부족합니다.")

    elif chart_type == "산점도":
        num_cols = df.select_dtypes(include=np.number).columns.tolist()
        if len(num_cols) >= 2:
            x_col = st.selectbox("X축 변수 선택", num_cols, key="scatter_x")
            y_col = st.selectbox("Y축 변수 선택", [c for c in num_cols if c != x_col], key="scatter_y")
            st.write(f"### {x_col} vs {y_col} 산점도")
            chart = alt.Chart(df).mark_circle(size=60).encode(
                x=x_col,
                y=y_col,
                tooltip=num_cols
            ).interactive()
            st.altair_chart(chart, use_container_width=True)
        else:
            st.warning("산점도를 그릴 수치형 변수가 2개 이상 필요합니다.")

    elif chart_type == "상자그림":
        num_cols = df.select_dtypes(include=np.number).columns.tolist()
        cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
        if num_cols:
            y_col = st.selectbox("상자그림으로 볼 수치형 변수 선택", num_cols)
            if cat_cols:
                x_col = st.selectbox("(선택) 그룹화할 범주형 변수 선택", ["없음"] + cat_cols)
                if x_col != "없음":
                    st.write(f"### {x_col}별 {y_col}의 상자그림")
                    chart = alt.Chart(df).mark_boxplot().encode(
                        x=x_col,
                        y=y_col
                    )
                else:
                    st.write(f"### {y_col}의 상자그림")
                    chart = alt.Chart(df).mark_boxplot().encode(
                        y=y_col
                    )
            else:
                st.write(f"### {y_col}의 상자그림")
                chart = alt.Chart(df).mark_boxplot().encode(
                    y=y_col
                )
            st.altair_chart(chart, use_container_width=True)
        else:
            st.warning("수치형 변수가 없습니다.")

# 1. 텍스트 요소
st.header("1. 텍스트 요소")  # 페이지의 섹션 헤더
st.subheader("1-1. 서브헤더")  # 작은 제목
st.text("이것은 일반 텍스트입니다.")  # 일반 텍스트
st.markdown("**마크다운** _지원_ :star:")  # 마크다운 지원
st.code("print('Hello, Streamlit!')", language="python")  # 코드 블록
st.latex(r"E=mc^2211121232323")  # LaTeX 수식

# 2. 데이터 표시
st.header("2. 데이터 표시")
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C'])
st.dataframe(df)  # 동적 데이터프레임
st.table(df.head(3))  # 정적 테이블
st.json({"key": "value", "number": 123})  # JSON 표시

# 3. 입력 위젯
st.header("3. 입력 위젯")
name = st.text_input("이름을 입력하세요")  # 텍스트 입력
age = st.number_input("나이", min_value=0, max_value=120, value=25)  # 숫자 입력
agree = st.checkbox("동의합니다")  # 체크박스
gender = st.radio("성별", ("남성", "여성", "기타"))  # 라디오 버튼
color = st.selectbox("좋아하는 색상", ["빨강", "초록", "파랑"])  # 셀렉트박스
colors = st.multiselect("좋아하는 색상(복수 선택)", ["빨강", "초록", "파랑"])  # 멀티셀렉트
date = st.date_input("날짜 선택")  # 날짜 입력
time = st.time_input("시간 선택")  # 시간 입력
file = st.file_uploader("파일 업로드")  # 파일 업로더
st.text_area("자기소개를 입력하세요")  # 텍스트 에어리어

# 4. 버튼 및 상호작용
st.header("4. 버튼 및 상호작용")
if st.button("클릭하세요"):  # 버튼
    st.write("버튼이 클릭되었습니다!")
progress = st.progress(0)  # 프로그레스 바
import time as t
for percent in range(0, 101, 20):
    progress.progress(percent)
    t.sleep(0.05)
st.slider("슬라이더", 0, 100, 50)  # 슬라이더

# 5. 미디어
st.header("5. 미디어")
st.image("https://placekitten.com/200/300", caption="고양이 이미지")  # 이미지
st.audio(
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    format="audio/mp3"
)  # 오디오
st.video(
    "https://www.w3schools.com/html/mov_bbb.mp4"
)  # 비디오

# 6. 사이드바
st.sidebar.title("사이드바 예시")  # 사이드바 제목
st.sidebar.button("사이드바 버튼")  # 사이드바 버튼

# 7. 기타
st.header("6. 기타")
with st.expander("더보기(Expander)"):
    st.write("이곳에 추가 정보를 넣을 수 있습니다.")  # Expander
st.success("성공 메시지")  # 성공 메시지
st.info("정보 메시지")  # 정보 메시지
st.warning("경고 메시지")  # 경고 메시지
st.error("에러 메시지")  # 에러 메시지
st.exception(Exception("예외 메시지 예시"))  # 예외 메시지

# 각주: 각 요소 옆에 주석으로 설명을 달았습니다.
