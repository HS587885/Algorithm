m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
import datetime

target_day = A

# 시작일과 종료일
start = datetime.date(2011, m1, d1)
end = datetime.date(2011, m2, d2)

# 요일 카운터
count = 0

# 반복문으로 날짜 순회
while start <= end:
    if start.strftime('%a') == target_day:
        count += 1
    start += datetime.timedelta(days=1)

print(count)

