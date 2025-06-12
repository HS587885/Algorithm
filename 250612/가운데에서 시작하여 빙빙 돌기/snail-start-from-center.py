n = int(input())
grid = [[0] * n for _ in range(n)]

# 방향: 오른쪽, 위, 왼쪽, 아래 (시계 반대)
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

x = y = n // 2
grid[x][y] = 1

num = 2
step = 1
dir_num = 0

while num <= n * n:
    for _ in range(2):  # 같은 step 수로 두 번 방향 전환
        for _ in range(step):
            x += dx[dir_num]
            y += dy[dir_num]
            if 0 <= x < n and 0 <= y < n:
                grid[x][y] = num
                num += 1
                if num > n * n:
                    break
        dir_num = (dir_num + 1) % 4
        if num > n * n:
            break
    step += 1


for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()
