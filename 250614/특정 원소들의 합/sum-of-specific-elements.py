import sys

input = sys.stdin.readline


arr_2d = [
    list(map(int, input().split()))
    for _ in range(4)
]

total = 0
cnt = 0
for i in range(len(arr_2d)):
    cnt += 1
    lst = arr_2d[i][:cnt]
    total += sum(lst)
    
print(total)  
