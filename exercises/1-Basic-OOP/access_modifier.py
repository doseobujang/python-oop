class MyClass:
    "공개, 보호된, 비공개 변수를 가진 클래스 예제"

    def __init__(self) -> None:
        "클래스 초기화 메서드"
        # 1. Public Variable: 외부에서 자유롭게 접근 가능
        self.public_var: str = "공개 변수"

        # 2. Protected Variable: 외부에서 접근 가능하지만 내부 전용 권장(관례)
        self._protected_var: str = "보호된 변수"

        # 3. Private Variable: 이름 변환(Name Mangling)으로 외부 접근 차단
        self.__private_var: str = "비공개 변수"

    def print_vars(self) -> None:
        "클래스 내부에서 모든 변수 출력"
        print(f"Public Variable: {self.public_var}")
        print(f"Protected Variable: {self._protected_var}")
        print(f"Private Variable: {self.__private_var}")

# MyClass의 인스턴스 생성
obj: MyClass = MyClass()
print("-" * 30)

# 1. access public variable
print(f"외부 접근 - 공개 변수: {obj.public_var}") # 접근 가능

# 2. access protected variable
print(f"외부 접근 - 보호된 변수: {obj._protected_var}") # 접근 가능하나 지양

# 3. 비공개 변수 직접 접근 시도 -> 오류 발생
try:
    print(f"외부 접근 - 비공개 변수: {obj.__private_var}") # 접근 불가
except AttributeError as e:
    print(f"외부 접근 - 비공개 변수: 접근 불가 (오류 발생: {e})")

# 4. Name Mangling된 이름으로 비공개 변수 접근
print(f"외부 접근 - 변환된 이름 접근: {obj._MyClass__private_var}")

# 5. 속성 값 변경
obj.public_var = "공개 변수-수정"
obj._protected_var = "보호된 변수-수정"
obj.__private_var = "비공개 변수-수정" # 주의: 기존 속성을 바꾸는 게 아님

# 내부 값 확인
obj.print_vars() # 내부에서 확인하면 기존 비공개 변수 값은 그대로임

# 새로 생긴 속성 접근
print(f"외부 접근 - 새로 생긴 비공개 변수: {obj.__private_var}") # 새로 생긴 속성 접근 가능