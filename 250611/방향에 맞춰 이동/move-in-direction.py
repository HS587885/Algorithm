n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
direction = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.

x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
final_x, final_y  = 0,0
for i in range(len(direction)):
    if direction[i] == "N":
        nx, ny = x + dx[1], y + (dy[3] * dist[i])
    elif direction[i] == "E":
        nx, ny = x + (dx[0] * dist[i]), y + dy[0]
    elif direction[i] == "W":
        nx, ny = x + (dx[2] * dist[i]), y + dy[2]
    else:
        nx, ny = x + dx[3], y + (dy[1] * dist[i])
    
    final_x += nx
    final_y += ny

print(final_x,final_y)