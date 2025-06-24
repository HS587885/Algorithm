import sys

input = sys.stdin.readline

lst1 = [list(map(int, input().split())) for _ in range(3)]
empty = list(map(int, input().split()))
lst2 = [list(map(int, input().split())) for _ in range(3)]
answer = [[0] * 3 for _ in range(3)]

for i in range(len(answer)):
    for j in range(len(answer[0])):
        answer[i][j] = lst1[i][j] * lst2[i][j]

for row in answer:
    print(*row)
