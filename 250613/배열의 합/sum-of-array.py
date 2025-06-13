import sys

input = sys.stdin.readline

for _ in range(4):
    arr_1d = list(map(int, input().split()))
    print(sum(arr_1d))



