from pathlib import Path
from dotenv import dotenv_values
from openai import OpenAI

env_path = Path(__file__).resolve().with_name("key_info.env")
print("키 파일 경로:", env_path)

if not env_path.is_file():
    print("❌ 파일이 없습니다. keytest.py와 같은 폴더에 넣으세요.")
else:
    api_key = dotenv_values(
        env_path, encoding="utf-8-sig"
    ).get("OPENAI_API_KEY")

    if not api_key or not api_key.strip():
        print("❌ 파일은 있지만 OPENAI_API_KEY 값이 없거나 비어 있습니다.")
    else:
        print("✅ 키 읽기 성공")
        try:
            client = OpenAI(api_key=api_key.strip(), timeout=30.0)
            response = client.responses.create(
                model="gpt-5-mini",
                input="'연결 성공!'이라고 짧게 답해주세요.",
            )
            print("✅ API 연결 성공")
            print(response.output_text)
        except Exception as e:
            print("❌ 테스트 실패:", e)