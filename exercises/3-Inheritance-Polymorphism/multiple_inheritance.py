# 첫 번째 부모 클래스: Flyer
class Flyer:
    # 하늘을 나는 능력을 가진 클래스
    def fly(self):
        print("하늘을 납니다.")

# 두 번째 부모 클래스: Swimmer
class Swimmer:
    # 수영할 수 있는 능력을 가진 클래스
    def swim(self):
        print("수영합니다.")

# 자식 클래스: Duck
# Flyer와 Swimmer 클래스 모두 상속받음
class Duck(Flyer, Swimmer):
    def quack(self):
        print("꽥꽥 소리를 냅니다.")
    
# Duck 클래스 인스턴스 생성
my_duck = Duck()

# 다중 상속을 통해 물려받은 메서드 사용
print("오리의 능력: ")
my_duck.fly()
my_duck.swim()
my_duck.quack()