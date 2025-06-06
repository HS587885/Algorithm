lst = list(map(int, input().split()))

for i in range(len(lst)):
    if lst[i] % 3 == 0:
        print(lst[i-1])
        break
