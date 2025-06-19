import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 그래프 구성
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 방문 표시
visited = [False] * (n + 1)

def dfs(v):
    visited[v] = True
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)

# 1번 정점에서 시작
dfs(1)

# 1번 제외하고 도달할 수 있는 정점 수 세기
print(sum(visited) - 1)
