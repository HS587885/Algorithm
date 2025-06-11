commands = input().strip()

# 북, 동, 남, 서
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0
dir_num = 0  # 북쪽

for cmd in commands:
    if cmd == "L":
        dir_num = (dir_num - 1 + 4) % 4
    elif cmd == "R":
        dir_num = (dir_num + 1) % 4
    else:  # 'F'
        x += dx[dir_num]
        y += dy[dir_num]

print(x, y)
