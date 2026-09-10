from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="간단한 CRUD API")


# 데이터 모델 정의
class Item(BaseModel):
    name: str
    price: int
    description: Optional[str] = None # 선택 : 설명 ( 안적으면 기본값 None 처리 )


# 임시 데이터베이스 및 ID 발급용 변수
fake_db = {} # 데이터를 저장할 빈 딕셔너리 ( 서버가 꺼지면 초기화 )
current_id = 1 # 새 아이템이 생길 때마다 부여할 고유 번호표

# 데이터 생성 : POST
@app.post("/items/")
def create_item(item: Item):
    global current_id # 함수 밖에 있는 current_id 값을 변경하기 위해 선언

    # Pydantic 모델(item)을 객체상태인데 파이썬 딕셔너리로 변환 ( Pydantic V2 권장 방식 )
    new_data = item.model_dump()
    # 알맹이(딕셔너리) 안에 자기 자신의 번호표(id)를 추가해 줌
    new_data["id"] = current_id
    # 가짜 DB에 데이터 저장(예: fake_db[1] = {'name': '사과', 'price': 1000, 'id': 1})
    fake_db[current_id] = new_data

    new_id = current_id # 방금 저장한 번호를 기억해 둠
    current_id += 1 # 다음 사람을 위해 번호표를 1 증가시킴

    return {"message": "아이템 생성 성공", "item_id": new_id, "data": fake_db[new_id]}

# 전체 데이터 조회 : GET
@app.get("/items/")
def read_all_items():
    return {"전체 아이템 목록": fake_db}

# 특정 단일 데이터 조회 : GET
@app.get("/items/{item_id}")
def read_item(item_id: int):
    # 찾는 번호가 DB에 없으면 에러(404 Not Found) 발생
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="아이템을 찾을 수 없습니다.")

    # 찾는 번호가 있으면 해당 데이터를 보여줌
    return {"item_id": item_id, "data": fake_db[item_id]}

# 데이터 수정 : PUT
@app.put("/items/{item_id}")
def update_item(item_id:int, item: Item):
    # 수정할 번호가 DB에 없으면 에러 발생
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="수정할 아이템을 찾을 수 없습니다.")

    # 새로 받은 데이터를 딕셔너리로 변환
    updated_data = item.model_dump()
    # 수정된 데이터에도 번호표(id)를 잊지 않고 다시 달아줌
    updated_data["id"] = item_id
    #기본 DB에 있던 데이터를 새로운 데이터로 덮어쓰기 ( 수정 완료 )
    fake_db[item_id] = updated_data

    return {"message": "아이템 수정 완료", "data": fake_db[item_id]}


# 데이터 삭제 : DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # 삭제할 번호가 DB에 없으면 에러 발생
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="삭제할 아이템을 찾을 수 없습니다.")

    # DB에서 해당 번호의 데이터를 뽑아내면서(삭제하면서) 변수에 저장
    #(.pop() 함수는 딕셔너리에서 데이터를 빼낼 때 사용)
    delete_item = fake_db.pop(item_id)
    # 삭제 완료 메시지와 방금 지워진 데이터를 돌려줌
    return {"message": f"{item_id}번 아이템 삭제 완료", "deleted_data": delete_item}
