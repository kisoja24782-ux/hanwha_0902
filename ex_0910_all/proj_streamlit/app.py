import streamlit as st
import requests

FASTAPI_URL = "http://127.0.0.1:8000"   # 올 대문자 상수는 항상 같은 값을 가짐 

st.title("Streamlit & FastAPI 연결 예제")

# 입력 폼 구성
with st.form("user_form"): # 열고 닫아야 하는 애들 알아서 닫아줌
    name = st.text_input("이름", value="홍길동")
    age = st.number_input("나이", min_value = 1, max_value=120, value=20) # 잘못된값이 들어오면 화면에서 막아야함
    submit_button = st.form_submit_button("백엔드로 전송")

if submit_button:  # 버튼 누를 때
    payload = {    # 딕트 형식으로 저장이 됨
        "name": name,
        "age": age
    }

    try:
        #FastAPI / predict 엔드포인트에 POST 요청

        response = requests.post(f"{FASTAPI_URL}/predict",json = payload) # 8000번 포트에 프레딕으로 요청을 보내라 json을 가져가서

        if response.status_code == 200: # 성공하면 
            result = response.json()
            st.success("FastAPI 응답성공!")
            st.write(f"**결과:** {result['result_message']}")  # ** 주변 결과글씨가 두꺼워짐
        else:
            st.error(f"오류 발생 ( 상태 코드 : {response.status_code})")

    except requests.exceptions.ConnectionError:  # 백단서버가 멈춤
        st.error("FastAPI 서버에 연결할 수 없습니다. 백엔드 서버가 실행 중인지 확인해 주세요")
