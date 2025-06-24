import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lst1 = [list(map(int, input().split())) for _ in range(n)]
lst2 = [list(map(int, input().split())) for _ in range(n)]
answer = [[0] * m for _ in range(n)]


for i in range(len(lst1)):
    for j in range(len(lst1[0])):
        if lst1[i][j] == lst2[i][j]:
            answer[i][j] = 0
        else:
            answer[i][j] = 1

for row in answer:
    print(*row)