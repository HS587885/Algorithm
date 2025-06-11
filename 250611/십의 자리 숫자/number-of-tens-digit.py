import sys

numbers = list(map(int, sys.stdin.readline().split()))

count = [0] * 10  # 인덱스 1~9만 사용

for num in numbers:
    if num == 0:
        break
    if num >= 10:
        tens = num // 10
        if 1 <= tens <= 9:
            count[tens] += 1

for i in range(1, 10):
    print(f"{i} - {count[i]}")
