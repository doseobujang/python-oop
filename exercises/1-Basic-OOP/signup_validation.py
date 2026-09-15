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