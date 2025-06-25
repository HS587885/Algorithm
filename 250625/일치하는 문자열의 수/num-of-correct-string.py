import sys

input = sys.stdin.readline

a,b = map(str, input().split())
a = int(a)
lst = [input().strip() for _ in range(a)]
answer = len([i for i in lst if i == b])
print(answer)