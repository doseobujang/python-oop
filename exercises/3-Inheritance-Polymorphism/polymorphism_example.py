# 부모 클래스: Animal
class Animal:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def speak(self) -> None:
        # 동물의 소리를 내는 공통 메서드
        print(f"{self.name}가 소리를 냅니다.")

# 자식 클래스: Dog
class Dog(Animal):
    # speak 메서드 오버라이딩
    def speak(self) -> None:
        # 개소리 메서드 오버라이딩
        print(f"{self.name}가 멍멍 짖습니다.")

# 자식 클래스: Cat
class Cat(Animal):
    # speak 메서드 오버라이딩
    def speak(self) -> None:
        # 고양이 소리 메서드 오버라이딩
        print(f"{self.name}가 야옹하고 웁니다!")

# 다양한 동물을 담을 리스트
animals = [Dog("바둑이"), Cat("나비"), Animal("어떤 동물")]

# 리스트를 순회하며 각 객체의 speak() 메서드 호출
for animal in animals:
    # 동일한 코드를 사용하지만, 각 객체의 타입에 따라 다른 동작을 함
    animal.speak() # 동일 코드, 다른 동작 -> 다형성