"""
요구사항:
filter()와 람다를 사용해 is_premium이 True인 프리미엄 사용자만 추출하고 리스트로 만드세요.

map()과 람다를 사용해 모든 사용자의 id만 추출하고 리스트로 만드세요.

is_active()라는 이름의 제너레이터 함수를 만드세요. 이 함수는 users 리스트를 순회하며 status가 'active'인 사용자만 yield로 반환해야 합니다.

힌트: lambda user: user['is_premium']와 같이 딕셔너리 키를 람다의 인자로 사용할 수 있습니다. 제너레이터 함수는 return 대신 yield를 사용합니다.
"""

users = [
    {'id': 'user01', 'is_premium': False, 'status': 'active'},
    {'id': 'user02', 'is_premium': True, 'status': 'inactive'},
    {'id': 'user03', 'is_premium': False, 'status': 'active'},
    {'id': 'user04', 'is_premium': True, 'status': 'active'}
]

# 1. filter()와 람다를 사용해 프리미엄 사용자 추출
premium_users = list(filter(lambda user: user['is_premium'], users))
print(f"프리미엄 사용자: {premium_users}")

# 2. map()과 람다를 사용해 사용자 ID만 추출
user_ids = list(map(lambda user: user['id'], users))
print(f"모든 사용자 ID: {user_ids}")

# 3. 제너레이터 함수를 사용해 active 상태의 사용자만 반환
def is_active(user_list):
    for user in user_list:
        if user['status'] == 'active':
            yield user

# 제너레이터 사용 예제
print("\n--- 'active' 사용자 목록 ---")
active_users = is_active(users)
for user in active_users:
    print(user)