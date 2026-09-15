class MyClass:
    "공개, 보호된, 비공개 속성을 pythonic하게 관리하는 클래스"

    def __init__(self) -> None:
        self.public_var = "공개 변수" # 외부 접근 허용
        self._protected_var = "보호된 변수" # 외부 접근 자제 (관례)
        self.__private_var = "비공개 변수" # property로만 접근

    @property
    def private_var(self) -> str:
        "비공개 변수 Getter"
        return self.__private_var
    
    @private_var.setter
    def private_var(self, value: str) -> None:
        "비공개 변수 Setter: 값 검증 등 로직 추가 가능"
        if not isinstance(value, str):
            raise TypeError("private_var는 문자열이어야 합니다.")
        if not value:
            raise ValueError("private_var는 빈 문자열일 수 없습니다.")
        self._private_var = value

    # 읽기 전용 속성 예시
    @property
    def readonly_info(self) -> str:
        "읽기 전용 속성: setter 없음"
        return f"{self.public_var}/{self._protected_var}"

# 사용 예시
if __name__ == "__main__":
    obj = MyClass()

    # 공개/보호 속성 (보호는 접근 가능하다 지양)
    print(f"공개: {obj.public_var}")
    print(f"보호(지양): {obj._protected_var}")

    # 비공개 속성: 속성처럼 접근(내부적으로 getter 호출)
    print(f"비공개(get): {obj.private_var}")

    # 비공개 속성 변경(내부적으로 setter 호출, 검증 수행)
    obj.private_var = "새 비공개 값"
    print(f"비공개(set 후): {obj.private_var}")

    # 읽기 전용 속성
    print(f"읽기 전용: {obj.readonly_info}")

    # 잘못된 값 설정 시 예외
    try:
        obj.private_var = "" # ValueError
    except ValueError as e:
        print("예외(ValueError): ", e)

    try:
        obj.private_var = 123 # TypeError
    except TypeError as e:
        print("예외(TypeError):", e)

"""
왜 이 방식이 실무에서 권장될까요?
캡슐화 + 검증: 값을 바꾸기 전에 타입/내용을 검증 가능
가독성: 외부에서는 obj.private_var처럼 속성 문법으로 깔끔하게 사용
유연성: 나중에 내부 구현을 바꿔도 외부 인터페이스(속성 이름)는 그대로 유지
읽기 전용 속성도 손쉽게 제공(@property만 두고 setter 생략)

@property를 쓰는 이유
권장사항이지 강제는 아님
속성 접근을 메서드처럼 제어할 수 있으면서도 외부에서는 변수 접근 문법처럼 깔끔하게 사용할 수 있음
"""