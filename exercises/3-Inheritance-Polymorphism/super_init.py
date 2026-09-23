class Animal:
    # 동물의 기본 정보를 관리하는 부모 클래스

    def __init__(self, name: str) -> None:
        # 동물 이름 초기화
        self.name: str = name
        print(f"부모 클래스: {self.name} 생성")

class Dog(Animal):
    # Animal 클래스를 상속받아 개 정보를 관리하는 자식 클래스

    def __init__(self, name: str, breed: str) -> None:
        """
        개 객체 초기화
        Args:
            name: 개 이름
            breed: 개 품종
        """
        # 부모 클래스 초기화 -> name 속성 초기화
        super().__init__(name)

        # Dog 클래스만의 고유한 속성
        self.breed: str = breed
        print(f"자식 클래스: {self.name} ({self.breed}) 생성")

if __name__ == "__main__":
    # Dog 객체 생성
    my_dog: Dog = Dog("바둑이", "진돗개")