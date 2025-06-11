numbers = list(map(int, input().split()))

count = [0] * 10  # index 1~9 사용

for num in numbers:
    if num >= 10:  # 두 자리 수만
        tens = num // 10
        count[tens] += 1

for i in range(1, 10):
    print(f"{i} - {count[i]}")