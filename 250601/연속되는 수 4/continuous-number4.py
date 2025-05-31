n = int(input())
arr = [int(input()) for _ in range(n)]

max_len = 1
current_len = 1

for i in range(1, n):
    if arr[i] > arr[i - 1]:
        current_len += 1
        max_len = max(max_len, current_len)
    else:
        current_len = 1

print(max_len)

