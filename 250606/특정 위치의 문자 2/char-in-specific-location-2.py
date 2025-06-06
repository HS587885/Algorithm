lst = list(map(str, input().split()))
for i in range(len(lst)):
    if i == 1 or i == 4 or i == 7:
        print(lst[i], end = ' ')