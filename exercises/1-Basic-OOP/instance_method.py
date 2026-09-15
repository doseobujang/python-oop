class Dog:
    "강아지를 나타내는 클래스"

    def __init__(self, name: str, age: int) -> None:
        """인스턴스 생성 시 이름과 나이 초기화

        Args:
            name (str): 강아지 이름
            age (int): 강아지 나이
        """

        self.name: str = name
        self.age: int = age

    def bark(self) -> None:
        "강아지가 짖는 동작 출력"
        print(f"{self.name}가 멍멍 짖습니다!")

    def get_info(self) -> str:
        "강아지의 이름과 나이 출력"
        print(f"이름: {self.name}, 나이: {self.age}살")

# Dog 클래스의 인스턴스 두 개 생성
dog1: Dog = Dog("바둑이", 3)
dog2: Dog = Dog("초코", 5)

# 각 인스턴스의 매서드 호출
print("--dog1 object--")
dog1.bark()
dog1.get_info()

print("\n--dog2 object--")
dog2.bark()
dog2.get_info()