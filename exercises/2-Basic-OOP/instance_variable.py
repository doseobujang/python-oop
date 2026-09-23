class Dog:
    def __init__(self, name, breed):
        # name과 breed는 인스턴스 변수
        self.name = name
        self.breed = breed
        self.tricks = []  # 빈 리스트도 인스턴스 변수 될 수 있음
    
    def add_trick(self, trick):
        self.tricks.append(trick)

# 서로 다른 두 개의 인스턴스 생성
dog1 = Dog("바둑이", "진돗개")
dog2 = Dog("멍멍이", "시츄")

# 각 인스턴스는 고유한 변수 값을 가짐
print(f"dog1의 이름: {dog1.name}, 품종: {dog1.breed}")
print(f"dog2의 이름: {dog2.name}, 품종: {dog2.breed}")

# 각 인스턴스에 고유한 기술 추가
dog1.add_trick("손")
dog2.add_trick("앉아")
dog2.add_trick("빵애에요")

print(f"\ndog1의 기술: {dog1.tricks}")
print(f"dog2의 기술: {dog2.tricks}")