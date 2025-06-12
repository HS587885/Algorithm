def reflect_slash(direction):
    if direction == 0: return 1
    if direction == 1: return 0
    if direction == 2: return 3
    return 2

def reflect_backslash(direction):
    if direction == 0: return 3
    if direction == 3: return 0
    if direction == 1: return 2
    return 1

def get_next_direction(direction):
    if direction == 0: return [1, 0]     # down
    if direction == 1: return [0, -1]    # left
    if direction == 2: return [-1, 0]    # up
    return [0, 1]                        # right

def is_in_bounds(x, y, size):
    return 0 <= x < size and 0 <= y < size

n = int(input())

mirror_grid = [list(input()) for _ in range(n)]
light_path = [[0] * n for _ in range(n)]

entry_index = int(input()) - 1
entry_dir = entry_index // n
entry_pos = entry_index % n

if entry_dir == 0:
    x, y = 0, entry_pos
elif entry_dir == 1:
    x, y = entry_pos, n - 1
elif entry_dir == 2:
    x, y = n - 1, n - entry_pos - 1
else:
    x, y = n - entry_pos - 1, 0

current_dir = entry_dir
step_count = 0

while True:
    step_count += 1
    light_path[x][y] = step_count

    if mirror_grid[x][y] == "/":
        current_dir = reflect_slash(current_dir)
    else:
        current_dir = reflect_backslash(current_dir)

    dx, dy = get_next_direction(current_dir)
    x += dx
    y += dy

    if not is_in_bounds(x, y, n):
        break

print(step_count)
