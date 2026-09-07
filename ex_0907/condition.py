# 1. 원본 데이터 리스트 준비
# 질문 3개가 들어있는데, 중간에 "" (완전 빈 문자열)이 섞여 있음
questions = ["asyncio란?", "", "FastAPI란?"]

# 깨끗한 데이터만 담을 빈 바구니(리스트) 준비
# type hint (list[str]) 를 써서 이 바구니에는 문자열만 담을거야 선언
valid_questions: list[str] = []

# 원본 리스트에서 질문을 하나씩 꺼내서 검사 시작
for question in questions:

    cleaned = question.strip() # 공백 제거(문자열 양 끝에 띄어쓰기나 줄바꿈 제거)

    # 빈 문자열 걸러내기(if not)
    # 파이썬에서 빈 문자열("")은 조건문에서 거짓(Flase) 으로 취금
    # if not cleaned: 는 만약 cleaned가 텅 비어있다면 ? 이라는 뜻
    if not cleaned: 
        # continue를 만나면 그 아래 코드는 무시하고 바로 다음 차례로 넘어감
        # 즉, 빈 문자열은 바구니에 담지 않고 패스하겠다는 뜻
        continue

    # 검사를 통과한(비어있지 않은) 깨끗한 질문만 새 바구니에 추가
    valid_questions.append(cleaned)

# 최종 결과 확인
# 중간에 있던 "" 빈 문자열이 완벽하게 걸러지고 2개만 남음
print(valid_questions)