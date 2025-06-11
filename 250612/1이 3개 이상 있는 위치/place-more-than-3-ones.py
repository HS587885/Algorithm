n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

result = 0

for i in range(n):
    for j in range(n):
        cnt = 0
        for d in range(5):
            ni = i + dx[d]
            nj = j + dy[d]
            if 0 <= ni < n and 0 <= nj < n:
                if grid[ni][nj] == 1:
                    cnt += 1
        if cnt >= 3:
            result += 1

print(result)
