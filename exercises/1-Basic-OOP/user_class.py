"""
# 사용자 정보 입력 받기
user_id = input("아이디를 입력하세요 (4글자 이상): ")
password = input("비밀번호는 입력하세요 (8글자 이상): ")
email = input("이메일 주소를 입력하세요 (@ 포함): ")

if len(user_id) < 4:
    print("오류: 아이디는 4글자 이상이어야 합니다.")
elif len(password) < 8:
    print("오류: 비밀번호는 8글자 이상이어야 합니다.")
elif '@' not in email:
    print("오류: 이메일 주소에 @ 기호가 포함되어야 합니다.")
else:
    print("회원가입이 완료되었습니다!")
"""

class User:
    def __init__(self, user_id, password) -> None:
        self.user_id = user_id
        self.password = password
        print(f"새로운 유저 '{self.user_id}'가 생성")
    
    def login(self, password):
        if self.password == password:
            print(f"'{self.user_id}'님, 로그인 성공!")
            return True
        else:
            print("로그인 실패: 비밀번호가 일치하지 않습니다")
            return False

    def change_password(self, password):
        self.password = password
        print(f"'{self.user_id}'님의 비밀번호가 변경")

# 클래스 사용 예제
if __name__ == "__main__":
    # 1. User 객체 생성
    my_user = User("doseobujang", "12345678")
        
    # 2. 올바른 비밀번호로 로그인 시도
    my_user.login("12345678")

    # 3. 틀린 비밀번호로 로그인 시도
    my_user.login("아오")

    # 4. 비밀번호 변경
    my_user.change_password("87654321")
    
    # 5. 변경된 비밀번호로 다시 로그인
    my_user.login("87654321")
    my_user.login("12345678")