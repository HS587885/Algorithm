import sys

a,b = map(int, sys.stdin.readline().split())
answer = (a+b) / (a-b)
print(("%.2f" % round(answer,2)))