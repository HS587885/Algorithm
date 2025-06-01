lst = [int(input()) for _ in range(10)]
cnt = 0
for i in range(len(lst)):
    if lst[i] % 2 != 0:
        cnt += 1

print(cnt)
