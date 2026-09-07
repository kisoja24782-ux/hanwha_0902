from typing import Annotated, Literal
from annotated_types import Gt
from pydantic import BaseModel

class Fruit(BaseModel):
  name: str
  color: Literal['red','green'] # 색상은 무조건 'red' 아니면 'green'이어야 합니다.
  #  다른 문자열이 들어오면 즉시 에러
  weight: Annotated[float, Gt(0)]
  #무게는 실수형(float)이되, 반드시 0보다 커야(Gt, Greater than) 합니다. 음수가 들어오는 것을 원천 차단
  bazam: dict[str, list[tuple[int, bool, float]]]
  # 딕셔너리인데 키는 문자열이고, 값은 리스트인데, 그 리스트 안에는 
  # 반드시 (정수, 불리언, 실수) 순서로 이루어진 튜플이 들어가야 해


print(
    Fruit(
        name = 'Apple',
        color = 'red',
        weight = 4.2,
        bazam = {'foobar': [(1, True, 0.1)]},
    )
)