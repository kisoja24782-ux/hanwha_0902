from fastapi import FastAPI
from enum import Enum

class ModelName(str, Enum): # 모델 네임, Enum : 열거형
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    기타 = "기타"


app = FastAPI()

# http://localhost:8000/users/me
@app.get("/users/me")  # 요청 request
async def read_user_me(): # 받음 response
    return {"user_id": "the current user"}

# # http://localhost:8000/uesrs/사용자
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"사용자 아이디user_id": user_id}

# @app.get("/users")
# async def read_users():
#     return ["Rick", "Morthy"]

# @app.get("/users")
# async def read_users2():
#     return ["Bean", "Elfo"]


# http://localhost:8000/models/
@app.get("/models/{model_name}")  # /model/ 뒤에 alexnet, lenet, resent 만 받음 class로 정의
async def get_model(model_name: ModelName):

    # 키를 요청하면 값을 return 함
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "키 요청 , 안녕하세요"}

    # 값을 요청하면 키를 return 함
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "값 요청, 반갑습니다."}

    # 그 외에 상황
    return {"model_name": model_name, "message": "쉽지 않다"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# http://localhost:8000/items/
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]  # [0:1] 하면 FOO 만 나옴



@app.get("/items2/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

