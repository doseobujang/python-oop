import sqlite3

class DatabaseConnection:
    _instance = None

    def __new__(cls, db_path=":memory:"):
        if cls._instance is None:
            print("DB 연결을 생성합니다.")
            cls._instance = super().__new__(cls)
            cls._instance.connection = sqlite3.connect(db_path)
        else:
            print("기존 DB 연결을 반환합니다.")
        return cls._instance

# 첫 번째 연결
db1 = DatabaseConnection("example.db")

# 두 번째 연결 시 이미 만들어진 연결을 사용
db2 = DatabaseConnection("example.db")

print(db1.connection is db2.connection) # True