class Config:
    _instance = None

    def __new__(cls, **kwargs):
        if cls._instance is None:
            print("Config 객체 생성")
            cls._instance = super().__new__(cls)
            cls._instance.settings = kwargs
        return cls._instance

# 첫 번째 설정
config1 = Config(debug=True, db_host="localhost")

# 두 번째 설정 시 이미 존재하느 객체 반환
config2 = Config(api_key="secret")

print(config1.settings)
print(config2.settings)