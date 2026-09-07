from datetime import date
from pydantic import BaseModel, Field, EmailStr, model_validator, computed_field, ConfigDict

class AdvancedUser(BaseModel):
    # ConfigDict로 모델의 행동을 엄격하게 제어
    model_config = ConfigDict(
        str_strip_whitespace= True, # 모든 문자열 양끝 공백 자동 제거
        extra= 'forbid',  #정의되지 않은 쓰레기 데이터가 들어오면 에러 발생
        populate_by_name= True # alias 이름과 원래 변수명 모두로 데이터 입력 가능
    )

    # Alias (별칭) 매핑
    # 외부 API 는 주로 camelCase(emailAddress)를 쓰지만, 파이썬은 snake_case(user_email)를 씀
    user_email: EmailStr = Field(alias="emailAddress")
    password: str = Field(min_length= 8)
    password_confirm: str = Field(min_length=8)
    birth_date: date


    # @model_validator (여러 필드를 엮어서 검사)
    # @field_validator 가 필드 1개만 검사했다면, 이건 모델 전체 필드를 엮어서 비교할 수 있음
    @model_validator(mode= 'after')
    def check_passwords_match(self) -> 'AdvancedUser':
        if self.password != self.password_confirm:
            raise ValueError('비밀번호와 비밀번호 확인이 일치하지 않습니다.')
        return self


    # @computed_field (계산된 필드)
    # 입력받지 않고 기존 데이터(생년월일)을 조합해 새로운 필드(나이)를 만들어서 반환
    @computed_field
    @property

    def age(self) -> int:
        today = date.today()
        # 생일이 지났는지 여부에 따라 나이를 정확히 계산
        age_calc = today.year - self.birth_date.year - ((today.month,
        today.day) < (self.birth_date.month, self.birth_date.day))
        return age_calc


# 실행 예시
# 클라이언트(웹) 에서 넘어온 날것의 JSON 데이터라고 가정
raw_data = {
    "emailAddress" : "   developer@example.com     ", # 공백이 들어있고 , 키 이름이 alias와 동일함
    "password" : "SuperSecret123!",
    "password_confirm" : "SuperSecret123!",
    "birth_date" : "1995-08-15"
}

# 데이터 변환 및 검증 시작
user = AdvancedUser(**raw_data)

print(user.model_dump())