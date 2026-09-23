# 부모 클래스: Animal
class Animal:
    # 모든 동물의 공통 특징을 정의하는 부모 클래스

    def __init__(self, name: str) -> None:
        # 동물 이름 초기화
        self.name: str = name

    def speak(self) -> None:
        # 동물마다 다른 소리를 내는 메서드 (기본 동작)
        print("...") # 기본적으로는 아무 소리도 내지 않음

# 자식 클래스: Dog
class Dog(Animal):
    # Animal 클래스를 상속받는 개 클래스

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def speak(self) -> None:
        print(f"{self.name}가 멍멍 짖습니다!")

# 자식 클래스: Cat
class Cat(Animal):
    # Animal 클래스를 상속받는 고양이 클래스

    def __init__(self, name:str) -> None:
        super().__init__(name)

    def speak(self) -> None:
        print(f"{self.name}가 야옹하고 웁니다!")

if __name__ == "__main__":
    # Animal, Dog, Car 객체 생성
    generic_animal: Animal = Animal("어떤 동물")
    my_dog: Dog = Dog("바둑이")
    my_cat: Cat = Cat("나비")

    # 각 객체의 speak() 메서드 호출 (다형성 확인)
    generic_animal.speak()
    my_dog.speak()
    my_cat.speak()

