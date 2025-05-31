n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
max_cnt = 0
current_cnt = 0
for i in range(1, n):
    if arr[i] > t and arr[i-1] > t:
        current_cnt += 1
        max_cnt = max(max_cnt, current_cnt)    
    else:
        current_cnt = 1
        

print(max_cnt)
