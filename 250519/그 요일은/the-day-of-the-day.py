def solution(m1, d1, m2, d2, A):
    # 2024년 각 월의 일수
    days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 요일을 숫자로 변환 (월요일: 0, 화요일: 1, ...)
    day_to_num = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}
    target_day = day_to_num[A]
    
    # 시작일부터 종료일까지의 총 일수 계산
    total_days = 0
    
    # m1월 d1일부터 m2월 d2일까지의 일수 계산
    if m1 == m2:
        total_days = d2 - d1 + 1
    else:
        # m1월의 남은 일수
        total_days += days_in_month[m1] - d1 + 1
        
        # m1+1월부터 m2-1월까지의 일수
        for month in range(m1 + 1, m2):
            total_days += days_in_month[month]
        
        # m2월의 일수
        total_days += d2
    
    # A요일의 개수 계산
    count = 0
    for i in range(total_days):
        # (시작일이 월요일(0)이므로 i를 더한 후 7로 나눈 나머지가 target_day와 같으면 A요일)
        if (i % 7) == target_day:
            count += 1
    
    return count

# 입력 예시
m1, d1, m2, d2 = map(int, input().split())
A = input().strip()

# 결과 출력
print(solution(m1, d1, m2, d2, A))
