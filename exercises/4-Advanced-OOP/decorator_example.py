from functools import wraps

# 1. 데코레이터 함수 정의
def my_decorator(func):
    """
    데코레이터 함수를 매개변수로 받아서
    원래 함수 실행 전후에 추가 동작을 넣을 수 있게 해줌
    """

    @wraps(func) # 원래 함수 이름과 docstring을 보존
    def wrapper():
        # 함수 실행 전 추가할 동작
        print("함수 실행 전 준비 작업")

        # 원래 함수를 실행
        func()

        # 함수 실행 후 추가할 동작
        print("함수 실행 후 추가할 동작")
    
    # wrapper 함수를 반환
    return wrapper

# 2. @ 문법으로 데코레이터 적용
# 아래 코드는 say_hello = my_decorator(say_hello)와 동일
@my_decorator
def say_hello():
    # 인사 메시지를 출력하는 원래 함수
    print("안녕하세요! 이것이 원래 함수입니다.")

# 3. 함수 실행
# 이제 say_hello()를 실행하면 wrapper()가 실행
say_hello()

# 4. 함수 메타데이터 확인
print(say_hello.__name__) # say_hello -> @wraps 덕분에 원래 이름 유지
print(say_hello.__doc__) # 인사 메시지를 출력하는 원래 함수 -> docstring 유지
# @wraps(func) 없으면 wrapper, None