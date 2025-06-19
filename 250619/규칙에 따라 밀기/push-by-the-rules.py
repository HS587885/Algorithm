from collections import deque
import sys

input = sys.stdin.readline

input_str = input().strip()
queries = list(input().strip())  

q = deque(input_str)

for i in queries:
    if i == "L":        
        q.rotate(-1)    
    else:  
        q.rotate(1)      

print(''.join(q))
