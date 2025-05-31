N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]
lst = {i:0 for i in list(set(student))}

# Please write your code here.
from collections import deque

s = deque(student)
while M > 0:
    std = s.popleft()
    M -= 1
    lst[std] += 1
    if lst[std] >= K:
        print(std)
        break
    



