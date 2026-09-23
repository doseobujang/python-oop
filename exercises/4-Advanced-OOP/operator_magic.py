class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        # + 연산자를 위한 매직 메서드
        # 두 Vector 객체의 x, y 값을 더한 새로운 Vector 객체 반환
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        # == 연산자를 위한 매직 메서드
        # 두 Vector 객체의 x, y 값이 모두 같으면 True 반환
        return self.x == other.x and self.y == other.y

# Vector 인스턴스 생성
v1 = Vector(2, 3)
v2 = Vector(5, 7)
v3 = Vector(2, 3)

# + 연산자 사용 (내부적으로 __add__ 호출)
v_sum = v1 + v2
print(f"v1 + v2 = {v_sum}")

# == 연산자 사용 (내부적으로 __eq__ 호출)
print(f"v1 == v2: {v1 == v2}")
print(f"v1 == v3: {v1 == v3}")