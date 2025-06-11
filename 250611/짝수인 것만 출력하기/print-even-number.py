import sys

n = int(input())
lst  = list(map(int, sys.stdin.readline().split()))

answer = [i for i in lst if i % 2 == 0]
print(*answer)