import datetime
from typing import Callable

# 외부 함수: 메시지 접두사를 설정하고 내부 함수를 반환
def logger_with_prefix(prefix: str) -> Callable[[str], None]:
    """
    주어진 접두사(prefix)를 기억하는 클로저 생성
    반환되는 내부 함수는 메시지를 받아 접두사와 함께 로그 출력
    """
    def log_message(message):
        # 내부 함수: 외부 함수의 'prefix' 변수를 기억하는 내부 함수(클로저)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{prefix}] {message}")
    return log_message

# -- 클로저 활용 예시 --
# 클로저 생성: 'API_CALL' 접두사를 가진 로그 함수
api_logger = logger_with_prefix("API_CALL")

# 클로저 생성: 'DB_QUERY' 접두사를 가진 로그 함수
db_logger = logger_with_prefix("DB_QUERY")

# 서로 다른 클로저를 사용해 로그 메시지 기록
print("-- API 로그 --")
api_logger("사용자 인증 요청 시작")
api_logger("사용자 인증 성공")

print("\n-- DB 로그 --")
db_logger("데이터베이스 연결 시도")
db_logger("사용자 정보 조회")

# 새로운 로그 함수 생성
error_logger = logger_with_prefix("ERROR")
error_logger("인증 토큰 만료 오류 발생")