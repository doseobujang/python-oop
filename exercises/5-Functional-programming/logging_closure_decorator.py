from functools import wraps
import datetime

def logger_with_prefix(prefix: str):
    """
    prefix 값을 기억하는 데코레이터 생성
    함수 실행 전후에 자동으로 로그 남김
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] [{prefix}] 함수 '{func.__name__}' 실행 시작")
            result = func(*args, **kwargs)
            print(f"[{timestamp}] [{prefix}] 함수 '{func.__name__}' 실행 시작")
            return result
        return wrapper
    return decorator

# -- 데코레이터 사용 예 --
@logger_with_prefix("API_CALL")
def authenticate_user(username: str):
    print(f"사용자 {username} 인증 처리 중...")

@logger_with_prefix("DB_QUERY")
def fetch_user_data(username: str):
    print(f"사용자 {username} 정보 조회 중...")

authenticate_user("alice")
fetch_user_data("alice")