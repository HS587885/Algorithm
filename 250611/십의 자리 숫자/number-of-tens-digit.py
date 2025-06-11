from collections import Counter

numbers = list(map(int, input().split()))

# 두 자리 수(10 이상)만 대상으로 십의 자리 추출
tens_digits = [num // 10 for num in numbers if num >= 10]

# 개수 세기
count = Counter(tens_digits)

# 출력
for i in range(1, 10):
    print(f"{i} - {count[i]}")
