# Pydantic 핵심 개념 정리

본 문서는 실무에서 활용되는 Pydantic의 데이터 검증 및 변환 핵심 개념들을 정리한 문서입니다.

## 1. 기본 검증과 자동 타입 변환 (Type Coercion)
*   **자동 변환:** 모델에 `age: int`로 정의되어 있을 때, 문자열 `"25"`가 입력되어도 Pydantic이 자동으로 정수형 `25`로 변환해 줍니다.
*   **선택적 입력과 기본값:** `nickname: str | None = None`과 같이 타입을 지정하면, 데이터가 들어오지 않았을 때 자동으로 `None`을 채워줍니다.

## 2. Field를 이용한 정밀 검증
`Field`를 사용하여 단순한 타입을 넘어 상세한 제약 조건을 설정할 수 있습니다.
*   **크기/길이 제한:** `age: int = Field(ge=0, le=150)` (0 이상 150 이하), `username: str = Field(min_length=3, max_length=20)` 등 강력한 유효성 검사가 가능합니다.
*   **API 요청 검증:** 외부(웹 등)에서 들어오는 데이터를 검증할 때, `def signup(data: SignupRequest):`처럼 함수 매개변수에 모델을 타입 힌트로 지정하여 안전하게 데이터를 처리합니다.

## 3. 중첩 모델 (Nested Models)과 복잡한 타입
*   **중첩 모델:** 딕셔너리 대신 미리 정의한 `Address` 모델을 메인 `User` 모델 안에 통째로 넣어 계층적인 데이터를 안전하게 관리합니다.
*   **리스트 내 중첩:** `items: List[Product]` 처럼 리스트 안에 다른 객체를 넣어 반복되는 구조도 빈틈없이 검증할 수 있습니다.
*   **고급 타입 제어:** 
    *   `Literal['red', 'green']`: 지정된 특정 문자열만 허용합니다.
    *   `Annotated[float, Gt(0)]`: 실수형이되 0보다 커야 함을 보장합니다.
    *   복잡한 자료구조 (`dict[str, list[tuple[int, bool, float]]]`)도 완벽히 검증 가능합니다.

## 4. 커스텀 유효성 검사기 (Custom Validators)
*   **`@field_validator`:** 기본 검증 외에 "비밀번호에 대문자 포함" 같은 자체 비즈니스 로직(정규표현식 등)을 만들 때 사용합니다. 조건에 맞지 않으면 `ValueError`를 발생시켜 깔끔하게 검증 에러로 처리합니다.

## 5. 데이터 내보내기 (Serialization/Dump)
*   **`model_dump()`:** Pydantic 객체를 파이썬 딕셔너리로 변환합니다.
    *   `exclude_unset=True`: 객체를 만들 때 직접 입력하지 않은 값(기본값 등)은 제외합니다.
    *   `exclude={'where'}`: 특정 필드를 콕 집어서 제외합니다.
*   **`model_dump_json()`:** 딕셔너리가 아닌 JSON 문자열 형태로 바로 변환하여 출력합니다.