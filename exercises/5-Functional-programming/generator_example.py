# Generator 함수
def count_up_to(max_num):
    print("제너레이터 시작!")
    n = 1
    while n <= max_num:
        # yield를 사용하여 값을 반환하고 실행을 잠시 멈춤
        yield n
        n += 1
    print("제너레이터 종료")

# 제너레이터 객체 생성
counter = count_up_to(5)

print("for 루프 시작")
for number in counter:
    print(f"현재 값: {number}")

print("for 루프 종료")

########################################

# 일반 함수: 한 번에 모든 결과 반환
def normal_func():
    return [1, 2, 3]

# 제네레이터 함수: yield를 사용해 중간 중간 결과 반환
def generator_func():
    yield 1
    yield 2
    yield 3

# 실행
print("일반 함수: ", normal_func())
print("제너레이터: ", list(generator_func()))