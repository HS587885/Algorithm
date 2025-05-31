from collections import deque

N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]
lst = {}

s = deque(student)
found = False  # <- 추가

while s:
    std = s.popleft()
    lst[std] = lst.get(std, 0) + 1
    if lst[std] == K:
        print(std)
        found = True
        break

if not found:
    print(-1)