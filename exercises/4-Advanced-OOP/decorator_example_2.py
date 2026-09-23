import time
from functools import wraps

# 실행 시간을 측정하는 데코레이터
def timer_decorator(func):
    @wraps(func) # 원래 함수의 이름과 실명을 보존
    def wrapper(*args, **kwargs):
        start_time = time.time() # 실행 시작 시간 기록
        result = func(*args, **kwargs) # 원래 함수 실행
        end_time = time.time() # 실행 종료 시간 기록
        print(f"'{func.__name__}' 실행시간: {end_time - start_time:.2f}초")
        return result # 원래 함수의 반환값 반환
    return wrapper # wrapper 함수를 반환

# 데코레이터 적용
@timer_decorator
def slow_task():
    # 시간이 걸리는 작업
    print("작업 시작...")
    time.sleep(2) # 2초 대기 (작업 시뮬레이션)
    print("작업 완료!")

# 함수 실행
slow_task()