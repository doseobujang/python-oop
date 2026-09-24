from abc import ABC, abstractmethod

# 추상 클래스 (동물의 공통 인터페이스)
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# 구체 클래스들
class Dog(Animal):
    def speak(self):
        print("멍멍")

class Cat(Animal):
    def speak(self):
        print("야옹")

# 팩토리 클래스
class AnimalFactory:
    def create_animal(self, animal_type: str) -> Animal:
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("알 수 없는 동물 종류입니다.")

# 사용 예시
factory = AnimalFactory()

my_dog = factory.create_animal("dog")
my_dog.speak()

my_cat = factory.create_animal("cat")
my_cat.speak()