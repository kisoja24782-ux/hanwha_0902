from pydantic import BaseModel

# 1. 기본: 데이터 검증과 타입 변환

class User(BaseModel):
    name: str # 이름은 문자열이어야 함
    age: int # 나이는 정수 이어야 함
    email: str # 이메일은 문자열이어야 함


user = User(
    name="Alice",
    age="25", # 실수로 문자열 25를 넣었지만 규칙을 보고 pydantic이 정수로 바꿔줌
    email="alice@example.com",
)

print(user) # 변환이 완료된 객체의 모습을 확인
print(user.age) # 객체 안의 나이만 뽑아서 출력
print(type(user.age)) # 진짜 정수로 바뀌었는지 타입을 확인

# ----------
# name='Alice' age=25 email='alice@example.com'
# 25
# <class 'int'>
# ----------