from datetime import datetime
from pydantic import BaseModel

class Meeting(BaseModel):
    when: datetime
    where: bytes # 바이트 형식으로 들어감
    why: str = 'No idea'

m = Meeting(when= '2020-01-01T12:00', where= 'home')
print(m.model_dump(exclude_unset= True))  # excldue : 제외시킨다
print(m.model_dump(exclude={'where'}, mode= 'json'))
print(m.model_dump_json(exclude_defaults= True))

