from collections import deque

s = input()
dq = deque(s)

dq.rotate(-1)  # 왼쪽으로 1칸 회전

print(''.join(dq))
