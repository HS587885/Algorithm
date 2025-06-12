n, m = map(int, input().split())

answer = [[0] * m for _ in range(n)]


dx = [1, 0, -1, 0]  # 아래, 오른쪽, 위, 왼쪽
dy = [0, 1, 0, -1]



x, y = 0, 0           # 시작은 (0, 0) 입니다.
dir_num = 0         # 0: 아래, 1: 오른쪽, 2: 위쪽, 3: 왼쪽

answer[x][y] = 1

# Please write your code here.
for i in range(2, n * m  + 1):
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]

    if not (0 <= nx < n and 0 <= ny < m) or answer[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4

    x,y = x + dx[dir_num], y + dy[dir_num]
    answer[x][y] = i

for i in range(n):
    for j in range(m):
        print(answer[i][j], end = ' ')
    print()

