# API요청 -> 검증 -> 데이터변환

from pydantic import BaseModel, Field


# 회원가입 요청 데이터 규칙(모델) 정의
# 외부(웹사이트 등) 에서 들어오는 회원가입 정보가 이 규칙을 통과해야만 인정됨
class SignupRequest(BaseModel):
    username: str = Field(min_length=3, max_length=20) # 문자열 길이 제한
    password: str = Field(min_length=8) # 비밀번호 8자리 이상
    age: int = Field(ge=14) # 나이는 14세 이상만


# 회원가입 처리 함수 : 함수 매개변수에 타입 힌트(data: SignupRequest) 지정
# 아무 딕셔너리나 받지 않고, 위에서 만든 '검증을 통과한 SignupRequest 객체'만 받겠다고 선언
def signup(data: SignupRequest):
    print("회원가입 처리")
    print(f"username: {data.username}") # 가입된 유저 이름
    print(f"age: {data.age}") # 가입된 유저 나이


# 데이터 입력 및 실행
# 규칙에 맞게 데이터를 넣어줌
# 만약 age = 10 혹은 password = 123을 넣으면 바로 에러가 터지면서 함수(signup)로 넘어가지도 못함
request = SignupRequest(
    username="alice",
    password="12345678",
    age= 25,
)

# 검증도니 request 객체를 함수에 넘겨줌
signup(request)