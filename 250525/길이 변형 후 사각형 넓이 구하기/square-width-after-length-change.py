import sys

a,b = map(int, sys.stdin.readline().split())
a += 8
b *= 3
for i in [a,b,(a*b)]:
    print(i)