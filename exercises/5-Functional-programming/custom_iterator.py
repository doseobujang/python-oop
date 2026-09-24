class MyNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        # iterator 객체 자신 반환
        return self

    def __next__(self):
        # 다음 요소 반환
        if self.current > self.end:
            # 더 이상 요소가 없으면 StopIteration 예외 발생
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

# MyNumbers 클래스의 인스턴스를 이터레이터로 사용
numbers = MyNumbers(1, 5)

for num in numbers:
    print(num)