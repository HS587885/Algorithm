import sys
from collections import deque

input = sys.stdin.readline

MAX = 20
MAX_Q = 55

dr = [-1, 0, 1, 0]  # ↑, →, ↓, ←
dc = [0, 1, 0, -1]

def insert(id, r1, c1, r2, c2):
    for r in range(r1, r2):
        for c in range(c1, c2):
            MAP[r][c] = id

def bfs(r, c):
    q = deque()
    q.append((r, c))
    visit[r][c] = True

    id = MAP[r][c]
    minR = maxR = r
    minC = maxC = c
    count = 1

    while q:
        cr, cc = q.popleft()
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < n and 0 <= nc < n and not visit[nr][nc] and MAP[nr][nc] == id:
                visit[nr][nc] = True
                q.append((nr, nc))
                minR = min(minR, nr)
                maxR = max(maxR, nr)
                minC = min(minC, nc)
                maxC = max(maxC, nc)
                count += 1

    return {
        'id': id,
        'minR': minR, 'minC': minC,
        'maxR': maxR, 'maxC': maxC,
        'count': count
    }

def find_live_micro():
    global micro
    for r in range(n):
        for c in range(n):
            visit[r][c] = False

    check = [False] * MAX_Q
    micro = []

    for r in range(n):
        for c in range(n):
            id = MAP[r][c]
            if id == 0 or dead[id] or visit[r][c]:
                continue
            m = bfs(r, c)
            if check[id]:
                dead[id] = True
            else:
                check[id] = True
                micro.append(m)

    micro[:] = [m for m in micro if not dead[m['id']]]

def sort_micro():
    micro.sort(key=lambda m: (-m['count'], m['id']))

def check_move(new_map, m, fr, fc):
    sr, sc, er, ec = m['minR'], m['minC'], m['maxR'], m['maxC']
    for r in range(sr, er + 1):
        for c in range(sc, ec + 1):
            if MAP[r][c] != m['id']:
                continue
            nr = fr - sr + r
            nc = fc - sc + c
            if nr >= n or nc >= n or new_map[nr][nc] != 0:
                return False
    return True

def move(new_map, m, fr, fc):
    sr, sc, er, ec = m['minR'], m['minC'], m['maxR'], m['maxC']
    for r in range(sr, er + 1):
        for c in range(sc, ec + 1):
            if MAP[r][c] != m['id']:
                continue
            nr = fr - sr + r
            nc = fc - sc + c
            new_map[nr][nc] = m['id']

def move_micro(new_map, m):
    for r in range(n):
        for c in range(n):
            if check_move(new_map, m, r, c):
                move(new_map, m, r, c)
                return

def move_all():
    global MAP
    new_map = [[0] * MAX for _ in range(MAX)]
    for m in micro:
        move_micro(new_map, m)
    MAP = [row[:] for row in new_map]

def get_count(id):
    for m in micro:
        if m['id'] == id:
            return m['count']
    return -1

def get_score(max_id):
    company = [[False] * MAX_Q for _ in range(MAX_Q)]

    for r in range(n):
        for c in range(n):
            if MAP[r][c] == 0:
                continue
            id1 = MAP[r][c]
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < n and 0 <= nc < n:
                    id2 = MAP[nr][nc]
                    if id2 != 0 and id1 != id2:
                        company[id1][id2] = True
                        company[id2][id1] = True

    score = 0
    for i in range(1, max_id):
        for j in range(i + 1, max_id + 1):
            if company[i][j]:
                score += get_count(i) * get_count(j)
    return score

def simulate():
    for id, (r1, c1, r2, c2) in enumerate(grid, start=1):
        insert(id, r1, c1, r2, c2)
        find_live_micro()
        sort_micro()
        move_all()
        print(get_score(id))


n, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(q)]

MAP = [[0] * MAX for _ in range(MAX)]
visit = [[False] * MAX for _ in range(MAX)]
dead = [False] * MAX_Q
micro = []

simulate()
