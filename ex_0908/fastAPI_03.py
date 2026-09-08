from fastapi import FastAPI
from enum import Enum


# 고정된 선택지 만들기 (Enum)
# 주소창에 아무 값이나 입력하지 못하게, 허용할 단어들을 미리 깐깐하게 정함
class ModelName(str, Enum): # 모델 네임, Enum : 열거형
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    기타 = "기타"


app = FastAPI() # 서버 열기

# 고정된 주소 ( 항상 변수 주소보다 위에 있어야 에러가 안남 )
# http://localhost:8000/users/me
@app.get("/users/me")  
async def read_user_me(): 
    # 클라이언트가 위 주소로 데이터를 요청(Request) 하면
    # 서버가 아래 데이터를 응답(Response) 으로 돌려줌
    return {"user_id": "the current user"}


# 변하는 주소 (만능 틀)
# # http://localhost:8000/uesrs/아무이름
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    # 주소창에 입력한 '아무이름'이 user_id 변수에 담겨서 그대로 출력됨
    return {"사용자 아이디user_id": user_id}

# @app.get("/users")
# async def read_users():
#     return ["Rick", "Morthy"]

# @app.get("/users")
# async def read_users2():
#     return ["Bean", "Elfo"]


# Enum 으로 검사하는 주소
# http://localhost:8000/models/ (미리 정해둔 이름들만 통과)
@app.get("/models/{model_name}")  # /model/ 뒤에 alexnet, lenet, resent 만 받음 class로 정의
async def get_model(model_name: ModelName):

    
    # Enum 객체 (ModelName.alexnet) 자체를 비교할 때는 파이썬 문법인 is 를 씀
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "키 요청 , 안녕하세요"}

   # Enum 객체가 가진 실제 '값(글자)'을 비교할 때는 '.value == "글자"' 를 씀
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "값 요청, 반갑습니다."}

    # 그 외에 상황
    return {"model_name": model_name, "message": "쉽지 않다"}

# 가짜 데이터베이스 ( 창고 )
# 실제 서버에서는 진짜 DB를 쓰지만, 연습용으로 3개의 데이터가 든 리스트를 만듬
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# 쿼리 매개변수 ( skip 과 limit ) - 데이터 잘라오기
# http://localhost:8000/items/?skip0&limit=1 처럼 물음표 뒤에 옵션을 담
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    # skip : 몇 개를 건너뛸지 ( 아무것도 안 적으면 기본값 0 )
    # limit : 몇 개를 가져올지 ( 아무것도 안 적으면 기본값 10 )
    return fake_items_db[skip : skip + limit]  # [0:1] 하면 FOO 만 나옴


# 경로 변수 + 선택적 쿼리 변수 합치기
# http://localhost:8000/items2/사과?q=빨강
@app.get("/items2/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    # item_id ( 경로 변수 )는 무조건 있어야 하고, q (쿼리 변수)는 없어도 상관없음
    if q:
        # 만약 손님이 주소창에 q 값을 적어서 보냈다면 이 줄이 실행됨
        return {"item_id": item_id, "q": q}

    # q 값이 없다면 if 문을 건너뛰고 이 줄이 실행되어 item_id 만 보여줌
    return {"item_id": item_id}

