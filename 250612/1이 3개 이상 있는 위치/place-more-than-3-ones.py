from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = len(grid)
m = len(grid[0])

x,y = 0,0
def bfs(x,y):
    q = deque([(x,y)])
    cnt = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                grid[nx][ny] = grid[x][y] + 1
                q.append((nx,ny))
                cnt += 1
       
    return cnt

max_cnt = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            max_cnt = max(max_cnt, bfs(i, j))

print(max_cnt)
