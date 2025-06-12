n, m = map(int, input().split())

# Please write your code here.
# dx = [1,0,-1,0]
# dy = [0,1,0,-1] # 아래, 오른쪽, 위쪽, 왼쪽
grid = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [0,1,0,-1] # 오른쪽, 아래, 왼,위
dy = [1,0,-1,0]

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

x,y = 0,0
dir_num = 0

grid[x][y] = alpha[0]
visited[x][y] = True

for i in range(1, n * m):
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]
    if not (0 <= nx < n and 0 <= ny < m) or grid[nx][ny] != 0 or visited == False:
        dir_num = (dir_num +1) % 4
    else:
        visited[nx][ny] = True

    x,y = x + dx[dir_num], y + dy[dir_num]
    grid[x][y] = alpha[i]


for i in range(n):
    for j in range(m):
        print(grid[i][j], end = ' ')
    print()