import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# 1. 텍스트 요소
st.header("1. 텍스트 요소")  # 페이지의 섹션 헤더
st.subheader("1-1. 서브헤더")  # 작은 제목
st.text("이것은 일반 텍스트입니다.")  # 일반 텍스트
st.markdown("**마크다운** _지원_ :star:")  # 마크다운 지원
st.code("print('Hello, Streamlit!')", language="python")  # 코드 블록
st.latex(r"E=mc^22332323")  # LaTeX 수식

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
