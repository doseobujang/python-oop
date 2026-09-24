class Singleton:
    _instance = None # 클래스 변수로 인스턴스 저장

    def __new__(cls):
        # __new__ 메서드를 오버라이딩하여 인스턴스 생성 제어
        if cls._instance is None:
            print("싱글턴 객체를 생성")
            cls._instance = super(Singleton, cls).__new__(cls)
        else:
            print("이미 생성된 객체 반환")
        return cls._instance

# 첫 번째 객체 생성
s1 = Singleton()

# 두 번째 객체 생성 시 이미 존재하는 객체가 반환됨
s2 = Singleton()

print(f"\ns1 == s2: {s1 is s2}")