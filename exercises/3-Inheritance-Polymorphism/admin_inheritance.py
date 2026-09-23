"""
요구사항:

Admin 클래스는 User 클래스를 상속받아야 합니다.

Admin의 __init__ 메서드는 User의 __init__을 호출하여 아이디와 비밀번호를 초기화해야 합니다. 추가적으로, 권한(permission) 인자를 받아 인스턴스 변수로 저장하세요.

login() 메서드를 오버라이딩하여, 로그인 성공 시 "관리자 로그인 성공! 권한: [권한]" 메시지를 출력하도록 변경하세요.

delete_user()라는 새로운 메서드를 추가하여, "사용자 삭제 권한이 있습니다." 메시지를 출력하도록 하세요.

힌트:
super().__init__(아이디, 비밀번호)를 사용해 부모 클래스의 생성자를 호출합니다.

"""

class User:
    def __init__(self, user_id, password) -> None:
        self.user_id = user_id
        self.password = password
        print(f"새로운 유저 '{self.user_id}'가 생성")
    
    def login(self, password) -> bool:
        if self.password == password:
            print(f"'{self.user_id}'님, 로그인 성공!")
            return True
        else:
            print("로그인 실패: 비밀번호가 일치하지 않습니다")
            return False

    def change_password(self, password):
        self.password = password
        print(f"'{self.user_id}'님의 비밀번호가 변경")

class Admin(User):
    def __init__(
        self,
        user_id: str,
        password: str,
        permission: Literal["read_only", "full_access"]
    ) -> None:
        super().__init__(user_id, password)
        self.permission: str = permission
        print(f"새로운 '{self.user_id}'가 생성되었습니다. 권한: {self.permission}")

    def login(self, password: str) -> bool:
        if self.password == password:
            print(f"관리자 로그인 성공! 권한: [{self.permission}]")
            return True
        else:
            print("로그인 실패: 비밀번호가 일치하지 않습니다.")
            return False
    
    def delete_user(self, target_user_id: str) -> None:
        print(f"관리자 '{self.user_id}'가 '{target_user_id}'를 삭제할 권한이 있습니다.")

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

##########################################################

    # 1. Admin 객체 생성
    admin_user = Admin("admin_master", "admin_pass", "full_access")

    print("\n--로그인 테스트--")
    # 2. 오버라이딩된 login 메서드 호출
    admin_user.login("admin_pass")

    print("\n--새로운 기능 테스트--")
    # 3. Admin 객체에만 있는 메서드 호출
    admin_user.delete_user("py_user_01")