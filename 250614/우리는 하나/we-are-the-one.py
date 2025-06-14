from collections import deque

n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 모든 위치 리스트
positions = [(i, j) for i in range(n) for j in range(n)]
answer = 0

def bfs(starts):
    visited = [[False]*n for _ in range(n)]
    q = deque(starts)
    for x, y in starts:
        visited[x][y] = True

    cnt = len(starts)

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                diff = abs(grid[x][y] - grid[nx][ny])
                if u <= diff <= d:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1
    return cnt


def combinations(n,arr, lst=None, start=0, result=None):
    if result is None:
        result = []
    if lst is None:
        lst = []
    if len(lst) == n:
        result.append(lst[:])  
        return
    for i in range(start, len(arr)):  
        combinations(n, arr, lst + [arr[i]], i + 1, result)
    return result

# 모든 시작점 조합
for starts in combinations(k, positions):
    answer = max(answer, bfs(starts))

print(answer)
