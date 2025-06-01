n = int(input())
sequence = list(map(int, input().split()))
from collections import deque

# Please write your code here.
lst = sorted(sequence)
s = deque(sequence)
answer = []
while s:
    num = s.popleft()
    order = lst.index(num)
    lst[order] = 'done'
    answer.append(order + 1)

print(*answer)


