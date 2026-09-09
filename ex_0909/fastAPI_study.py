from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="타이타닉 데이터")

class Titanic(BaseModel):
    person_number: int
    name: str
    sex: str
    age: Optional[int] = None
    fare: int  # 요금
    survived: int # 생존여부
    pclass: int # 객실등급
    ticket: int # 티켓 번호
    sibsp: int # 동반한 형제자매 및 배우자 수
    parch: int # 동반한 부모 및 자녀 수
    embarked: str # 탑승 항구 ( C, Q, S )

Titanic_db = {}
current_id = 1

@app.post("/titanic")
def create_person(person: Titanic):

    new_data = person.model_dump()
    new_data["id"] = current_id
    Titanic_db[current_id] = new_data

    new_person = current_id
    current_id += 1

    return {"message": "명단 생성 성공", "item_id": new_person, "data": Titanic_db[new_person]}

@app.get("/titanic/")
def read_all_person():
    return {"전체 타이타닉 명단 : ": Titanic_db}

@app.get("/titanic/{person_id}")
def read_person_number(number: int):
    if number not in Titanic_db:
        raise HTTPException(status_code=404, detail="아이템을 찾을 수 없습니다.")

    return {"person_id": number, "data": Titanic_db[number]}


# 데이터 수정 PUT
@app.put("/titanic/{person_id}")
def update_person(number: int, person: Titanic):

    if number not in Titanic_db:
        raise HTTPException(status_code=404, detail="수정할 사람을 찾을 수 없습니다.")

    updated_data = person.model_dump()
    updated_data["id"] = number
    Titanic_db[number] = updated_data

    return {"message": "사람 수정 완료", "data": Titanic_db[number]}


@app.delete("/titanic/{person_id}")
def delete_person(number: int):
    if number not in Titanic_db:
            raise HTTPException(status_code=404, detail="삭제할 사람을 찾을 수 없습니다.")

    delete_person = Titanic_db.pop(number)

    return {"message": f"{number}번 사람 삭제 완료", "deleted_data": delete_person}