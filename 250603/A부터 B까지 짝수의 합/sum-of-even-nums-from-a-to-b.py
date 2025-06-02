import sys

a,b = map(int, sys.stdin.readline().split())


lst = [i for i in range(a,b+1) if i % 2 ==0]
if lst == []:
    print(0)
else:
    total = sum(lst)
    print(total)