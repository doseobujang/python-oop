class A:
    def method(self) -> None:
        print("method of A")

class B(A):
    def method(self) -> None:
        print("method of B")

class C(A):
    def method(self) -> None:
        print("method of C")

# 다중 상속: B와 C를 모두 상속
class D(B, C):
    def method(self) -> None:
        print("method of D")

    def call_super(self) -> None:
        # super()를 통해 다음 MRO 순서의 메서드 호출
        super().method()

# D 클래스의 MRO 확인
print("D의 MRO 순서: ")
print(" -> ".join(cls.__name__ for cls in D.mro()))

# D 클래스 인스턴스 생성
d = D()

# D의 메서드 호출
d.method()

# super()를 통해 상위 클래스 메서드 호출
d.call_super()