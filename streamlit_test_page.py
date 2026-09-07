import streamlit as st
import pandas
import time

st.title("Welcome to SJ World")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")
st.title("Dashboard", icon=":material/dashboard:")

st.subheader("스트림릿 만들어 보자", divider= True)

st.markdown("여기 꽃이 있어요 &mdash;\:tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
st.divider()

st.write("내 목표 점수는 ?")

score = st.slider("설정해 보세요",0, 100, 25)
st.write("제 목표 점수는 ",score," 입니다.")
st.divider()

st.button("reset", type="primary")
if st.button("인사!"):
    st.write("반갑습니다.")
else:
    st.write("안녕")

st.write("다른 언어로 인사해 보아요")

if st.button("ALoha", type="secondary"):
    st.write("Ciao")

st.divider()

st.write("자동차가 어디 있을까요 ?")
left, middle, right = st.columns(3)

if left.button("1번 버튼", width="stretch"):
    left.markdown("여기는 자동차가 없어요")

if middle.button("2번 버튼",width="stretch"):
    middle.markdown("자동차가 있어요")

if right.button("THREE", width="stretch"):
    right.markdown("여기는 자동차가 없어요")


st.divider()

action = st.menu_button("강아지 찾기", options=["1번","2번","3번"])
if action == "1번":
    st.write("없어용")
elif action == "2번":
    st.write("멍멍!!")
elif action == "3번":
    st.write("없어용")

st.divider()

st.write("평점을 남겨주세요")

sentiment_mapping = ["one","two","three","four","five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")

st.divider()

if st.button("생일이신가요 ?"):
    st.toast("생일 축하 합니다~")
    time.sleep(1)
    st.toast("생일 축하 합니다~")
    time.sleep(1)
    st.toast("Congratulation",icon="🎉")