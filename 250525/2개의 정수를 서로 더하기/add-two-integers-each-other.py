import sys
a,b = map(int, sys.stdin.readline().split())
a = a + b
b =  b + a

print(a,b)