from pydantic import BaseModel, Field


# 1. 하위 모델 정의 ( Address )
# 메인 모델 안에 부품처럼 들어갈 "주소" 전용 규칙을 따로 만듬
class Address(BaseModel):
    city: str # 도시는 문자열
    zip_code: str # 우편번호도 문자열

# 메인 모델 정의 (User)
class User(BaseModel):
    name: str
    age: int = Field(ge= 0, le= 150) # Field를 이용한 조건 0 이상 150 이하 그 외는 에러를 발생시켜 막아줌
    email: str
    address: Address  # 핵심 포인트 : 딕셔너리 대신 위에서 만든 Address  모델 자체를 통째로 넣음
    nickname: str | None= None
    # 핵심 포인트 : 선택적 입력(Optional)과 기본값
    # str | None 은 문자열이 들어올 수도, 값이 안들어올 수도(None) 있다는 뜻
    # =None 을 통해 데이터를 안 넣으면 자동으로 None을 채워줌


# 데이터 입력 및 객체 생성
user = User(
    name= "Alice",
    age= 25,
    email= "alice@example.com",
    address={
        "city":"Dajeon",
        "zip_code": "34100",
    },
)

print(user)
print(user.address.city) # 중첩된 데이터를 점(.)을 연속해서 찍어 꺼내 씀
print(user.nickname) # 입력하지 않았던 항목이 기본값으로 잘 세팅되었는지 확인