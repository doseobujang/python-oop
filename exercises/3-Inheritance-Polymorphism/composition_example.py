# 엔진 클래스: 자동차가 가지고 있는(has-a) 기능
class Engine:
    def __init__(self, horsepower: int) -> None:
        self.horsepower = horsepower

    def start(self) -> None:
        print(f"엔진({self.horsepower} 마력)이 시동을 겁니다.")

    def stop(self) -> None:
        print("엔진이 정지합니다.")

class Car:
    # Car는 Engine을 포함하여 동작한다
    def __init__(self, name: str, engine: Engine) -> None:
        self.name = name
        self.engine = engine # 엔진을 외부에서 주입받음

    def start(self) -> None:
        print(f"{self.name} 시동 중...")
        self.engine.start()

    def stop(self) -> None:
        self.engine.stop()
        print(f"{self.name} 정지 완료.")

if __name__ == "__main__":
    performance_engine = Engine(1020)
    my_car = Car("테슬라 모델 S", performance_engine)
    my_car.start()
    my_car.stop()