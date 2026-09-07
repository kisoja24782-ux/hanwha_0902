from pydantic import BaseModel, Field, field_validator
from typing import List
import re

# class User(BaseModel):
#     name: str
#     age: int
#     email: str

# user = User(
#     name="Alice",
#     age="25",
#     email="alice@example.com",
# )

# print(user)
# print(user.age)
# print(type(user.age))

class User(BaseModel):
    id: int
    username: str
    is_active: bool = True # 입력하지 않으면 기본값 True 적용
# 1. 정상 데이터 입력 (문자열 "123"이 정수 123으로 자동 변환됨)
user_data = {"id": "123", "username": "alice"}
user = User(**user_data)
print(user.model_dump())


# Field를 이용한 정밀검증과 중첩모델(Nested Model)
class Product(BaseModel):
    name: str = Field(min_length = 2, max_length = 20)
    price: float = Field(gt= 0, description="가격은 0보다 커야 합니다.")

class Order(BaseModel):
    order_id: str
    items: List[Product] # List안에 Product 모델이 통째로 들어감

# 복잡한 딕셔너리 구조 검증
order_data = {
    "order_id" : "ORD-001",
    "items":[
        {"name": "Laptop", "price":1500.0},
        {"name": "Mouse","price":25.5}
    ]
}

order = Order(**order_data)
print(order.items[0].name)

#Field의 gt(초과), min_length(최소길이) 등을 이용해 강력한 제약조건을 만듬
#List 안에 또 다른 BaseModel을 넣어 깊숙한(Nested) 데이터구조까지 빈틈없이 체크 가능

class SignupForm(BaseModel):
    username: str
    password: str

    @field_validator('password')
    @classmethod
    def validate_password(cls, value: str) -> str:
        if len(value) < 8:
            raise ValueError('비밀번호는 최소 8자리 이상이어야 합니다.')
        if not re.search(r'[A-Z]', value):
            raise ValueError('비밀번호에 대문자가 1개 이상 포합되어야 합니다.')
        return value

# 아래 주석처럼 대문자가 없는 비밀번호를 넣으면 즉시 에러(ValidationError) 발생
# user = SignupForm(username="user1", password="password123")

# @field_validator 데코레이터를 붙인 함수를 만들면, 데이터가 들어올 때 내가 짠 파이선 코드 필터를
# 거치게 됩니다. 조건에 안 맞을 때 ValueError 를 발생시키면 Pydantic이 이를 깔끔한 검증 에러로
# 바꿔서 뱉어냅니다.