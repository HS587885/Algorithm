from collections import deque
import sys

input = sys.stdin.readline

word = input().strip()

q = deque(word)
print(''.join(q))
for _ in range(len(word)):
    q.rotate(1)
    print(''.join(q))
