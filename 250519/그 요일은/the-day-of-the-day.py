import datetime

# 입력
m1, d1, m2, d2 = map(int, input().split())
A  = input().strip()

# 시작일과 종료일 정의
start = datetime.date(2024, m1, d1)
end = datetime.date(2024, m2, d2)

# 요일 카운트
count = 0

# 날짜 순회하면서 요일 비교
while start <= end:
    if start.strftime('%a') == A:
        count += 1
    start += datetime.timedelta(days=1)

print(count)

