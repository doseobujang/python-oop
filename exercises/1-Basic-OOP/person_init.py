# Person 클래스 정의
class Person:
    def __init__(self, name, age):
        """
        __init__ 메서드: 객체가 생성될 때 호출
        name: 사람 이름
        age: 사람 나이
        """
        # 매개변수로 전달받은 값들을 인스턴스 속성으로 저장
        self.name = name
        self.age = age
    
    def introduce(self):
        "이름과 나이 출력하는 메서드"
        print(f"안녕하세요, 제 이름은 {self.name}이고, 나이는 {self.age}살입니다.")

# Person 클래스의 인스턴스 생성 및 초기화
# __init__ 메서드가 자동 호출, '이름'과 '나이' 전달
person1 = Person("이원석", 23)
person2 = Person("김수한무", 56)

# 각 인스턴스의 매서드 호출
person1.introduce()
person2.introduce()

# 인스턴스 속성에 접근
print(f"\n{person1.name}의 나이는 {person1.age}살입니다.")