numbers = [1, 2, 3, 4, 5]

# 각 숫자를 제곱하는 람다 함수를 map()에 적용
squared_numbers = list(map(lambda x: x**2, numbers))

print(f"원래 숫자: {numbers}")
print(f"제곱된 숫자: {squared_numbers}")