N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# 시작 위치
x, y = 0, 0

# 방향 맵 (서남북동)
dir_map = {
    "W": (-1, 0),
    "S": (0, -1),
    "N": (0, 1),
    "E": (1, 0)
}

# 시간 카운트
time = 0

# 이동 시뮬레이션
for i in range(N):
    dx, dy = dir_map[dir[i]]
    for _ in range(dist[i]):
        x += dx
        y += dy
        time += 1
        if x == 0 and y == 0:
            print(time)
            exit()

print(-1)
