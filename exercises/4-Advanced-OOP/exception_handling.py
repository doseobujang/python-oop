# 사용자 입력으로 숫자를 나누는 함수
def divide_numbers(a, b):
    try:
        # 예외가 발생할 수 있는 코드
        result = a / b
    except ZeroDivisionError:
        # ZeroDivisionError가 발생했을 때 처리
        print("오류: 0으로 나눌 수 없습니다.")
        return None
    except TypeError:
        # TypeError가 발생했을 때 처리
        print("오류: 숫자만 입력해주세요.")
        return None
    else:
        # 예외가 발생하지 않았을 때 실행
        print(f"나눗셈 결과: {result}")
        return result
    finally:
        # 예외 발생 여부와 관계없이 항상 실행
        print("나눗셈 연산이 완료되었습니다.\n")

# 다양한 경우로 함수 호출
divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers(10, "hello")