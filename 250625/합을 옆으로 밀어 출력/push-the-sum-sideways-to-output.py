import sys

input = sys.stdin.readline

n = int(input())
total = str(sum([int(input()) for _ in range(n)]))
first = total[0]
answer = total[1:]
print(answer + first)

