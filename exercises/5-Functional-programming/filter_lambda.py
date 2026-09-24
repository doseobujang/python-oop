numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 짝수만 필터링하는 람다 함수를 filter()에 적용
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(f"원래 숫자: {numbers}")
print(f"필터링된 짝수: {even_numbers}")