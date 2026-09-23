from abc import ABC, abstractmethod

# ABC(Abstract Base Class)를 상속받아 추상 클래스 정의
class Animal(ABC):
    # 모든 동물의 공통 인터페이스를 정의하는 추상 클래스
    def __init__(self, name: str) -> None:
        self.name: str = name

    # @abstractmethod 데커레이터를 사용하여 추상 메서드 선언
    @abstractmethod
    def speak(self) -> None:
        # 이 메서드는 반드시 자식 클래스에서 구현해야 함
        pass

    def sleep(self) -> None:
        # 추상 메서드가 아닌 일반 메서드도 포함할 수 있음
        print(f"{self.name}이(가) 잠을 잡니다.")

# Animal을 상속받는 Dog 클래스
class Dog(Animal):
    # 강아지 클래스
    def speak(self) -> None:
        # 추상 메서드 speak()를 반드시 구현해야 함
        print(f"{self.name}가 멍멍 짖습니다!")

# Animal을 상속받는 Cat 클래스
class Cat(Animal):
    # 고양이 클래스
    def speak(self) -> None:
        # 추상 메서드 speak()를 반드시 구현해야 함
        print(f"{self.name}가 야옹하고 웁니다!")

# 객체 생성 및 메서드 호출
my_dog = Dog("바둑이")
my_cat = Cat("나비")

my_dog.speak()
my_dog.sleep()

my_cat.speak()
my_cat.sleep()

# 다음 코드는 오류를 발생시킴
# an_animal = Animal("어떤 동물")
# TypeError: Can't instantiate abstract class Animal with abstract method speak