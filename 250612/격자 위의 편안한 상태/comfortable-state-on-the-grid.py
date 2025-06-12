# n: 격자 크기, m: 점의 개수
n, m = map(int, input().split())

points_to_color = [tuple(map(int, input().split())) for _ in range(m)]

grid = [[0] * n for _ in range(n)]

dr = [-1, 1, 0, 0] # row changes
dc = [0, 0, -1, 1] # column changes

for r, c in points_to_color:
    # 현재 점의 좌표를 0-based 인덱스로 변환합니다.
    # 문제의 좌표는 1-based, 리스트 인덱스는 0-based이므로 1을 빼줍니다.
    current_r, current_c = r - 1, c - 1

    # 해당 칸을 색칠합니다 (1로 표시).
    grid[current_r][current_c] = 1

    # 현재 색칠한 칸(current_r, current_c)의 인접한 칸에 색칠된 칸의 개수를 셉니다.
    adjacent_colored_count = 0
    for i in range(4):
        nr, nc = current_r + dr[i], current_c + dc[i]
        
        # 인접한 칸의 좌표가 격자 범위 안에 있는지 확인합니다.
        if 0 <= nr < n and 0 <= nc < n:
            # 인접한 칸에 다른 점(1)이 있는지 확인합니다.
            if grid[nr][nc] == 1:
                adjacent_colored_count += 1
    
    # '편안한 상태' 조건 확인: 인접한 색칠된 칸의 개수가 정확히 3개인지 확인
    if adjacent_colored_count == 3:
        print(1) # 편안한 상태이면 1 출력
    else:
        print(0) # 편안한 상태가 아니면 0 출력