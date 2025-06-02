import sys

a,b = map(int, sys.stdin.readline().split())
lst = sum([i for i in range(a,b+1) if i % 6 == 0 and i % 8 != 0])
print(lst)
