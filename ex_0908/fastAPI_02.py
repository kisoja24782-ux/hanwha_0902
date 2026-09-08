from fastapi import FastAPI
from pydantic import BaseModel # 데이터 양식은 검사해주는 도구

app = FastAPI() # 내 서버 만들기


# 수정할 때 사용할 '데이터 양식'을 만듬
# 손님이 데이터를 보낼 때 반드시 이 규칙을 지켜야 서버가 받아줌
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None # 할인 여부 ( 참/거짓(True/False))

# 기본 주소 접속 시 인사말을 건네는 창구
@app.get("/")
def read_root():
    return {"Hello": "World"}

# 특정 상품의 정보를 조회 하는 창구
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    # 주소창에서 item_id(만능 틀)를 받고, 물음표 뒤에서 q(쿼리)를 받음
    return {"item_id": item_id, "q": q}

# 특정 상품의 정보를 수정(PUT) 하는 창구
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    # item_id: int 주소창에서 몇 번 상품을 수정할 건지 번호를 받음
    # item: Item 전송된 데이터(Request Body)가 위에서 만든 'Item 양식' 에 맞는지 검사하고 받아옴
    return {"item_name": item.name, "item_id": item_id}
    # 수정된 데이터중에서 '상품 이름' 과 '상품 번호'만 뽑아서 보여줌