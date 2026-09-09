from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

fake_db = {
    1: {"name": "사과", "price": 1500},
    2: {"name": "바나나", "price": 2000},
    3: {"name": "포도", "price": 3000}
}

# 수정할 때 받을 데이터 구조 정의
class ItemUpdate(BaseModel):
    name: str
    price: int

class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None  

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users/me")
async def read_user_me():
    return{"user_id": " 현재 유저 아이디"}


@app.get("/users/{user_id}")
async def read_user(user_id : str):
    return {"사용자 아이디": user_id}

# my_data_list_db = [{"num1_data":"HOME", "num2_data":"LIFE","num3_data":"FAMILY"}]

# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return my_data_list_db[skip : skip + limit]

# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.model_dump()
#     if item.tax is not None:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict

# @app.get("/items/{user_item}")
# async def read_items(user_item : str):
#     return {"생성된 아이템 : ": user_item}

@app.post("/items/") # 화면이 없으면 post 로 테스트
def create_item(item: Item):
    return{
        "message": f"'{item.name}'아이템이 성공적으로 생성되었습니다.",
        "item_data":item
    }

# http://127.0.0.1:8000/items2/

@app.get("/items2/")
def get_items():
    return fake_db


@app.delete("/items2/{item_id}")
def delete_item(item_id: int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="해당 아이템을 찾을 수 없습니다.")

    delete_item = fake_db.pop(item_id)

    return {
        "message": f"{item_id}번 아이템이 성공적으로 삭제되었습니다.",
        "deleted_data": delete_item,
        "remaining_db": fake_db  # 남은 아이템 확인용
    }


# [확인용] 전체 데이터 보기 ( GET )
@app.get("/items/")
def get_items():
    return {"현재 DB": fake_db}

# 데이터 수정하기 ( PUT )
@app.put("/items/{item_id}")
def update_item(item_id: int, item: ItemUpdate):
    #아이템이 DB에 없는 경우 에러 발생
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="수정할 아이템이 없습니다.")

    # DB에 있는 기존 데이터를 새로 받은 데이터로 덮어쓰기 ( 수정 )
    fake_db[item_id] = {"name": item.name, "price": item.price}

    return {
        "message": f"{item_id} 번 아이템이 성공적으로 수정되었습니다.",
        "update_data": fake_db[item_id]

    }