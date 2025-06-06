lst = list(map(int, input().split()))
idx = 0
for i in range(len(lst)):
    if idx == lst[i]:
        idx = i
        break
lst = lst[:idx]
print(sum(lst[-3:]))