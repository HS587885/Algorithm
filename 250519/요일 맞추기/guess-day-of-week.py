m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
import datetime

# 기준 날짜 (월요일)
base_date = datetime.date(2011, m1, d1)

# 목표 날짜
target_date = datetime.date(2011, m2, d2)

# 날짜 차이 계산
delta = (target_date - base_date).days

# 요일 리스트 (월요일 기준)
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# 결과 출력
print(days[delta % 7])