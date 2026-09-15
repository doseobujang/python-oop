# 부모 클래스: Animal
class Animal:
    "동물의 기본 행동을 정의하는 부모 클래스"

    def __init__(self, name: str) -> None:
        "Animal 초기화 메서드"
        self.name: str = name
        print(f"새로운 동물 '{self.name}'이 생성되었습니다.")

    def eat(self) -> None:
        "먹이를 먹는 행동"
        print(f"{self.name}이(가) 먹이를 먹습니다.")

    def sleep(self) -> None:
        "잠을 자는 행동"
        print(f"{self.name}이(가) 잠을 잡니다.")

# 자식 클래스: Dog
class Dog(Animal):
    "Animal 클래스를 상속받는 개 클래스"

    def __init__(self, name: str, breed: str) -> None:
        "Dog 초기화 메서드"
        super().__init__(name)
        self.breed: str = breed
        print(f"'{self.name}'는 {self.breed}입니다.")

    def bark(self) -> None:
        "짖는 행동"
        print(f"{self.name}이(가) 멍멍 짖습니다.")

# 자식 클래스: Cat
class Cat(Animal):
    "Animal 클래스를 상속받는 고양이 클래스"

    def __init__(self, name: str, color: str) -> None:
        "Cat 초기화 메서드"
        super().__init__(name)
        self.color: str = color
        print(f"'{self.name}'는 {self.color}색 고양이입니다.")

    def meow(self) -> None:
        "울음소리 내는 행동"
        print(f"{self.name}이(가) 애용하고 울었습니다.")

if __name__ == "__main__":
    # Dog와 Cat 객체 생성
    my_dog: Dog = Dog("바둑이", "진돗개")
    my_cat: Cat = Cat("나비", "흰색")

    # 상속받은 메서드 사용
    my_dog.eat()
    my_cat.sleep()

    # 자식 클래스만의 고유한 메서드 사용
    my_dog.bark()
    my_cat.meow()