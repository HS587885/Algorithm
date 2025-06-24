import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num = 1
for i in range(n):
    row = []
    for j in range(m):
        row.append(num)
        num += 1
    print(*row)
