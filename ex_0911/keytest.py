import os   # 환경변수를 읽기 위한 모듈
import openai  # OpenAI 오류 종류를 구분하기 위한 모듈
from openai import OpenAI # API 요청에 사용할 클라이언트

def main():
    # 환경변수에서 키를 읽고 앞뒤 공백 제거
    # 키가 없으면 빈 문자열("") 반환
    api_key = os.getenv("OPENAI_API_KEY", "").strip()

    # 키가 없으면 안내 후 함수 종료
    if not api_key:
        print("❌ OPENAI_API_KEY 환경변수를 찾을 수 없습니다.")
        print("환경변수 설정 후 CMD 또는 VS Code를 다시 실행하세요.")
        return

    # 키 값 자체는 출력하지 않음
    print("✅ 환경변수에서 키를 읽었습니다.")

    try:
        # API 클라이언트 생성 : 이 단계에서는 요청을 보내지 않음
        client = OpenAI(
            api_key=api_key, # 인증에 사용할 API 키
            timeout=30.0, # 요청 타임아웃 설정(초)
            max_retries=0, # 실패 시 자동 재시도하지 않음
        )

        # 실제 모델 요청: API 사용 요금이 발생하는 부분
        response = client.responses.create(
            model="gpt-5-mini",
            input="'연결 성공!'이라고 짧게 답해주세요.", # 모델에 보낼 내용
        )

        # 요청이 완료되었고 응답 테스트가 있는지 확인
        if response.status == "completed" and response.output_text:
            print("✅ API 키와 모델이 정상 작동합니다.")
        else:
            print("⚠️ 응답 상태:", response.status)

        print("응답:", response.output_text)

        if response.usage:
            print("사용 토큰:", response.usage.total_tokens)

    except openai.AuthenticationError:
        print("❌ 인증 실패: API 키 값을 확인하세요.")

    except openai.RateLimitError as e:
        print("❌ 요청 한도 또는 API 크레딧 문제:", e.message)

    except openai.APIConnectionError as e:
        print("❌ 서버 연결 실패:", repr(e.__cause__))

    except openai.APIStatusError as e:
        print(f"❌ HTTP {e.status_code}:", e.message)

if __name__ == "__main__":
    main()