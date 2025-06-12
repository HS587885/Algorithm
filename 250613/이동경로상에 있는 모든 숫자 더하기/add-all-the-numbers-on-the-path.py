N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# 방향: 북(0), 동(1), 남(2), 서(3)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
current_dir = 0  # 북쪽으로 시작

# 시작 위치 (중앙)
row, col = N // 2, N // 2
total_sum = board[row][col]  # 시작 위치 값 추가

# 명령어 실행
for command in str:
    if command == 'L':
        current_dir = (current_dir - 1) % 4
    elif command == 'R':
        current_dir = (current_dir + 1) % 4
    elif command == 'F':
        # 현재 방향으로 이동 시도
        dr, dc = directions[current_dir]
        new_row, new_col = row + dr, col + dc
        
        # 격자 범위 내에 있는지 확인
        if 0 <= new_row < N and 0 <= new_col < N:
            row, col = new_row, new_col
            total_sum += board[row][col]

print(total_sum)
