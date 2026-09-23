class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        # 사용자에게 보여줄 문자열 표현
        return f"({self.x}, {self.y})"

    def __repr__(self):
        # 개발자에게 보여줄 객체 표현
        return f"Point(x={self.x}, y={self.y})"

# Point 클래스 인스턴스 생성
p = Point(3, 4)

# print() 함수는 __str__을 호출
print(p)

# repr() 함수는 __repr__을 호출
print(repr(p))

# 리스트에 객체를 담고 출력
print([p])