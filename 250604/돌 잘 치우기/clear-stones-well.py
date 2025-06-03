import sys
from collections import deque
from itertools import combinations

n, k, m = map(int, sys.stdin.readline().split())

grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

r = []
c = []
for _ in range(k):
    ri, ci = map(int, sys.stdin.readline().split())
    r.append(ri - 1)
    c.append(ci - 1)

# Please write your code here.
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(temp_grid):
    visited = [[False] * n for _ in range(n)]
    q = deque()
    cnt = 0
    
    # 모든 시작점을 큐에 추가
    for i in range(len(r)):
        if temp_grid[r[i]][c[i]] == 0 and not visited[r[i]][c[i]]:
            visited[r[i]][c[i]] = True
            q.append((r[i], c[i]))
            cnt += 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n and temp_grid[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1
    
    return cnt
                
# 모든 돌의 위치 찾기
stones = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            stones.append((i, j))

total = 0

# M개의 돌을 제거하는 모든 조합 시도
for stones_to_remove in combinations(stones, min(m, len(stones))):
    # 임시 격자 생성 (원본 grid 복사)
    temp_grid = [row[:] for row in grid]
    
    # 선택된 돌들 제거
    for stone_r, stone_c in stones_to_remove:
        temp_grid[stone_r][stone_c] = 0
    
    # BFS로 도달 가능한 칸 수 계산
    result = bfs(temp_grid)
    total = max(total, result)

print(total)

