import sys

arr = list(map(float, sys.stdin.readline().split()))
lst = []
for i in arr:
    if i == 0:
        break
    else:
        lst.append(int(i))
        
print(*reversed(lst))