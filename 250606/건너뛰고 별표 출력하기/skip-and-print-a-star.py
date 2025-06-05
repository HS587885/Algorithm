n = int(input())

for i in range(1, n + 1):
    print("*" * i)
    print()

# 아래쪽 삼각형
for i in range(n - 1, 0, -1):
    print("*" * i)
    print()