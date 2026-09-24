# 일반 함수 정의
def add(x, y):
    return x + y

# 람다 표현식으로 동일한 기능 구현
lambda_add = lambda x, y: x + y

print(f"일반 함수 결과: {add(5, 3)}")
print(f"람다 함수 결과: {lambda_add(5, 3)}")