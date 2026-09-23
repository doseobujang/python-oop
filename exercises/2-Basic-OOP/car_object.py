# Car 클래스 가져오기
from car_class import Car

# class를 바탕으로 객체 생성
my_car: Car = Car()
your_car: Car = Car()

# 생성된 객체의 메서드 호출
print("--my_car object--")
my_car.drive()
my_car.stop()

print("\n--your_car object--")
your_car.drive()
your_car.stop()