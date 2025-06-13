import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# Please write your code here.

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [[-1]*m for _ in range(n)]


def melt(time):
    q = deque([(0,0)])
    visited[0][0] = time

    cnt = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] != time:
                visited[nx][ny] = time
                if a[nx][ny] == 0:
                    q.append((nx,ny))
                elif a[nx][ny] == 1:
                    a[nx][ny] = 0
                    cnt += 1
    return cnt


time = 0
last = 0

while True:
    cnt = melt(time)
    if cnt == 0:
        break
    last = cnt
    time += 1

print(time, last)
