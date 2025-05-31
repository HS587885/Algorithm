N = int(input())
arr = [int(input()) for _ in range(N)]

max_cnt = 1
cnt = 1

for i in range(1, N):
    if (arr[i] > 0 and arr[i-1] > 0) or (arr[i] < 0 and arr[i-1] < 0):
        cnt += 1
        max_cnt = max(max_cnt, cnt)
    else:
        cnt = 1

print(max_cnt)
