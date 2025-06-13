import sys

input = sys.stdin.readline

for _ in range(5):
    arr_1d = list(map(str, input().split()))
    answer = [i.upper() for i in arr_1d]
    print(*answer)



