import sys

a,b = map(int, sys.stdin.readline().split())

if b > a:
    lst = [i for i in range(a,b+1) if i % 5 ==0]
    total = sum(lst)
    print(total)
else:
    lst = [i for i in range(b,a+1) if i % 5 ==0]
    total = sum(lst)
    print(total)