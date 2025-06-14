import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time_grid = [[-1] * n for _ in range(n)]
q = deque()

# 상한 귤 위치 큐에 넣고 시간 0으로 표시
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            q.append((i, j))
            time_grid[i][j] = 0

# BFS
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if grid[nx][ny] == 1 and time_grid[nx][ny] == -1:
                time_grid[nx][ny] = time_grid[x][y] + 1
                grid[nx][ny] = 2  # 상하게 만듦
                q.append((nx, ny))

# 출력
for i in range(n):
    row = []
    for j in range(n):
        if grid[i][j] == 0:
            row.append("-1")
        elif time_grid[i][j] == -1:
            row.append("-2")
        else:
            row.append(str(time_grid[i][j]))
    print(' '.join(row))
