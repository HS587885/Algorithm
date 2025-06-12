import sys
input = sys.stdin.readline

n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.

# 오른쪽, 위, 왼쪽, 아래
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

x = n // 2
y = n // 2

grid[x][y] = 1
dir_num = 0
cnt = 1
cur = 0

for i in range(1,n * n):
    nx, ny = x + dx[dir_num], y + dy[dir_num]
    if not (0 <= nx < n and 0 <= ny < n) or cur >= cnt or grid[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
        if dir_num == 0 or dir_num == 2:
            cnt += 1
        cur = 0

    
    x = x + dx[dir_num]
    y = y + dy[dir_num]
    grid[x][y] = i + 1
    cur += 1
    
for i in range(n):
    for j in range(n):
        print(grid[i][j], end = " ")
    print()