class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        # observer 등록
        self._observers.append(observer)

    def notify(self, message):
        # 모든 옵저버에 변경 사항 알림
        for observer in self._observers:
            observer.update(message)

class Observer:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"[{self.name}] 알림을 받았습니다: {message}")

# subejct와 observer 생성
subject = Subject()
observer1 = Observer("observer1")
observer2 = Observer("observer2")

# 옵저버 등록
subject.attach(observer1)
subject.attach(observer2)

# subject의 상태 변경
subject.notify("change!")