class Dog:
    # kind is class variable
    # 모든 Dog instance가 공유하는 값
    kind = "canine"

    def __init__(self, name):
        # name is instance variable
        self.name = name

# Dog class의 instance 두 개 생성
dog1 = Dog("바둑이")
dog2 = Dog("멍멍이")

# 클래스 변수는 클래스 이름 또는 인스턴스를 통해 접근 가능
print(f"dog1의 종류: {dog1.kind}")
print(f"dog2의 종류: {dog2.kind}")
print(f"클래스 이름으로 접근: {Dog.kind}")

# 클래스 변수 값 변경 (클래스 이름을 통해 변경하는 것이 올바른 방법)
Dog.kind = "canidae"

print("\n---클래스 변수 값 변경 후---")
print(f"dog1의 종류: {dog1.kind}")
print(f"dog2의 종류: {dog2.kind}")