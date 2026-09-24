"""
요구사항:

예외 처리:
사용자 입력 유효성 검사(1부 문제) 로직을 try-except 블록으로 감싸서, 유효성 검사 실패 시 ValueError 예외를 발생시키고 적절한 오류 메시지를 출력하세요.

데코레이터:
is_authenticated라는 이름의 데코레이터를 만드세요. 이 데코레이터는 사용자 로그인 여부를 확인하여 로그인되지 않았으면 "로그인이 필요합니다."라는 메시지를 출력합니다.
change_password() 메서드 위에 @is_authenticated 데코레이터를 적용하여, 로그인한 사용자만 비밀번호를 변경할 수 있도록 만드세요.

힌트:
raise ValueError("...")를 사용하여 예외를 발생시키고, except ValueError:로 예외를 잡습니다.
데코레이터는 클로저 개념을 활용하여 구현합니다.

"""

# 현재 로그인 상태를 저장할 전역 변수
# 실무에서는 세션이나 토큰 등으로 관리
IS_LOGGED_IN = False

# 1. 데코레이터 정의
def is_authenticated(func):
    # 사용자 로그인 여부를 확인하는 데코레이터
    def wrapper(*args, **kwargs):
        if IS_LOGGED_IN:
            # 로그인 상태면 원래 함수 실행
            return func(*args, **kwargs)
        else:
            # 로그인 상태가 아니면 오류 메시지 출력
            print("오류: 로그인이 필요합니다.")
            return None
    return wrapper

class User:
    def __init__(self, user_id, password) -> None:
        self.user_id = user_id
        self.password = password
        print(f"새로운 유저 '{self.user_id}'가 생성")
    
    def login(self, password) -> bool:
        global IS_LOGGED_IN
        if self.password == password:
            print(f"'{self.user_id}'님, 로그인 성공!")
            IS_LOGGED_IN = True
            return True
        else:
            print("로그인 실패: 비밀번호가 일치하지 않습니다")
            return False

    # 2. 데코레이터 적용
    @is_authenticated
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
    try:
        # 사용자로부터 정보 입력받기 (예외 처리 적용)
        user_id = input("아이디를 입력하세요 (4글자 이상): ")
        if len(user_id) < 4:
            raise ValueError("아이디는 4글자 이상이어야 합니다.")

        password = input("비밀번호를 입력하세요 (8글자 이상): ")
        if len(password) < 8:
            raise ValueError("비밀번호는 8글자 이상이어야 합니다.")

        email = input("이메일 주소를 입력하세요 (@ 포함): ")
        if '@' not in email:
            raise ValueError("이메일 주소에 @ 기호가 포함되어야 합니다.")

        my_user = User(user_id, password)

        # 1. 로그인 없이 비밀번호 변경 시도 -> 데코레이터에 의해 차단
        print("\n-- 로그인 없이 비밀번호 변경 시도 --")
        my_user.change_password("new_secure_password")

        # 2. 로그인 후 비밀번호 변경 시도 -> 성공
        print("\n-- 로그인 후 비밀번호 변경 시도 --")
        my_user.login(password)
        my_user.change_password("new_secure_password")

    except ValueError as e:
        print(f"회원가입 실패: {e}")

##########################################################

        # # 1. Admin 객체 생성
        # admin_user = Admin("admin_master", "admin_pass", "full_access")

        # print("\n--로그인 테스트--")
        # # 2. 오버라이딩된 login 메서드 호출
        # admin_user.login("admin_pass")

        # print("\n--새로운 기능 테스트--")
        # # 3. Admin 객체에만 있는 메서드 호출
        # admin_user.delete_user("py_user_01")