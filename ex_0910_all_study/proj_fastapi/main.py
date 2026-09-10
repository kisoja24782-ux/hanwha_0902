from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title = "Titanic API")

class Titanic(BaseModel):
    name: str
    sex: str
    age: Optional[int] = None
    fare: float
    survived: int
    pclass: int


# 연습용 데이터
titanic_db = {
    1: {
        "id": 1,
        "name": "Jack",
        "sex": "male",
        "age": 20,
        "fare": 7.25,
        "survived": 0,
        "pclass": 3
        },
    2: {
        "id": 2,
        "name": "Rose",
        "sex": "female",
        "age": 17,
        "fare": 71.2,
        "survived": 1,
        "pclass": 1
    }
    
}

current_id = 3

# 서버 확인
@app.get("/")
def read_root():
    return {"message": "FastAPI 서버 정상 작동"}

# 전체 승객 조회
@app.get("/titanic")
def get_all_passengers():
    return titanic_db

# 특정 승객 조회
@app.get("/titanic/{person_id}")
def get_passenger(person_id: int):

    if person_id not in titanic_db:
        raise HTTPException(status_code=404, detail="승객을 찾을 수 없습니다.")

    return titanic_db[person_id]


# 승객 추가
@app.post("titanic")
def create_passenger(person: Titanic):
    global current_id

    new_data = person.model_dump()

    new_data["id"] = current_id

    titanic_db[current_id] = new_data

    create_id = current_id

    current_id += 1

    return {"message": "승객 등록 성공", "data": titanic_db[create_id]}


# 승객 삭제
@app.delete("/titanic/{person_id}")
def delete_passenger(person_id: int):

    if person_id not in titanic_db:
        raise HTTPException(status_code=404, detail="삭제할 승객을 찾을 수 없습니다.")

    deleted_data = titanic_db.pop(person_id)

    return {"message": "삭제 성공", "data": deleted_data}


@app.get("/stats")
def get_stats():

    total = len(titanic_db)

    survived_count = 0

    for person in titanic_db.values():
        if person["survived"] == 1:
            survived_count += 1

    return {"total": total, "survived": survived_count, "dead":total - survived_count}