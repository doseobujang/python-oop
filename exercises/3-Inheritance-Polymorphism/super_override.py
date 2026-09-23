class Vehicle:
    # 차량의 기본 정보를 관리하는 부모 클래스

    def __init__(self, name: str, speed: int) -> None:
        """
        차량 객체 초기화
        Args:
            name: 차량 이름
            speed: 차량 속도(km/h)
        """

        self.name: str = name
        self.speed: int = speed

    def display_info(self) -> None:
        # 차량 정보 출력
        print(f"이름: {self.name}, 속도: {self.speed} km/h")

class ElectricVehicle(Vehicle):
    # 전기차 정보를 관리하는 자식 클래스

    def __init__(self, name: str, speed: int, battery_level: int) -> None:
        """
        전기차 객체 초기화
        Args:
            name: 전기차 이름
            speed: 속도 (km/h)
            battery_level: 배터리 잔량 (%)
        """
        super().__init__(name, speed)
        self.battery_level: int = battery_level

    def display_info(self) -> None:
        # 차량 정보와 배터리 잔량 출력
        super().display_info() # 부모 클래스의 메서드 호출
        print(f"배터리 잔량: {self.battery_level}%")

if __name__ == "__main__":
    # 전기차 객체 생성
    my_ev: ElectricVehicle = ElectricVehicle("테슬라 모델3", 200, 85)

    # 오버라이딩된 메서드 호출
    my_ev.display_info()