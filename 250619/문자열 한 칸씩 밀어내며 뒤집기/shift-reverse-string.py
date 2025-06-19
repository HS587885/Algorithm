from collections import deque
import sys

input = sys.stdin.readline

input_str, q = input().split()
q = int(q)
queries = [int(input()) for _ in range(q)]

# Please write your code here.
def f(input_str, query):
    q = deque(input_str)
    if query is 1:
        exception = q.popleft()
        q.append(exception)
        input_str = ''.join(q)
        return input_str
    elif query is 2:
        exception = q.pop()
        #q.rotate(1)
        q.appendleft(exception)
        input_str = ''.join(q)
        return input_str
        
    else:
        input_str = ''.join(reversed(input_str))
        return input_str

k = deque(queries)
while k:
    i = k.popleft()
    input_str = f(input_str,i)
    print(input_str)