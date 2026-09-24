# 딕셔너리 리스트
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 95}
]

# 1. 90점 이상인 학생만 필터링
passing_students = filter(lambda s: s["score"] > 90, students)
print(f"90점 이상 학생: {list(passing_students)}")

# 2. 학생 이름만 추출
student_names = map(lambda s: s["name"], students)
print(f"모든 학생 이름: {list(student_names)}")

# 3. 점수를 기준으로 내림차순 정렬
# sorted()의 key 인자에 람다 함수를 전달
sorted_students = sorted(students, key=lambda s: s["score"], reverse=True)
print(f"\n점수 순 정렬: {sorted_students}")