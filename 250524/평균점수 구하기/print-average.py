import sys

arr = list(map(float, sys.stdin.readline().split()))
answer = sum(arr)/ len(arr)
print(("%.1f" % answer))