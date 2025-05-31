from collections import deque

N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]
lst = {}

s = deque(student)
while s:
    std = s.popleft()
    lst[std] = lst.get(std, 0) + 1
    if lst[std] == K:
        print(std)
        break



