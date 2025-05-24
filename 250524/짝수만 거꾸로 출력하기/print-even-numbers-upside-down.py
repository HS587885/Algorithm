import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
rev_arr = list(reversed(arr))
answer = [i for i in rev_arr if i % 2 == 0]
print(*answer)
   