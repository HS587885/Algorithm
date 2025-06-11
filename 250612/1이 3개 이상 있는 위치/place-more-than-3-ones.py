n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

for i in range(n):
    for j in range(n):
        count = 0
        for d in range(4):  # 자기 자신 제외하고 4방향만 탐색
            ni = i + dx[d]
            nj = j + dy[d]
            if 0 <= ni < n and 0 <= nj < n:
                if grid[ni][nj] == 1:
                    count += 1
        if count >= 3:
            result += 1

print(result)
