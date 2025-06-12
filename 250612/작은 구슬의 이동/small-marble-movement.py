# 입력
n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# 방향 정의 및 매핑
dir_map = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
dxs = [-1, 1, 0, 0]  # U, D, L, R
dys = [0, 0, -1, 1]
dir_num = dir_map[d]

# 시뮬레이션
for _ in range(t):
    nx = r + dxs[dir_num]
    ny = c + dys[dir_num]

    # 범위를 벗어나면 방향만 반대로 바꾸고 위치는 그대로
    if not (1 <= nx <= n and 1 <= ny <= n):
        if dir_num == 0: dir_num = 1
        elif dir_num == 1: dir_num = 0
        elif dir_num == 2: dir_num = 3
        elif dir_num == 3: dir_num = 2
    else:
        # 정상적으로 이동
        r, c = nx, ny

# 출력
print(r, c)
