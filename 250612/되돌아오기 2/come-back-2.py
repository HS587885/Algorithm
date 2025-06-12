commands = input().strip()

# Please write your code here.
# 북, 동, 남, 서
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0
dir_num = 0  # 북쪽
times = 0
for cmd in commands:
    times += 1
    if cmd == "L":
        dir_num = (dir_num - 1 + 4) % 4
    elif cmd == "R":
        dir_num = (dir_num + 1) % 4
    else: 
        x += dx[dir_num]
        y += dy[dir_num]
    if x == 0 and y == 0:
        print(times)
        break
   


    
