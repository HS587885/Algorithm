import sys

lst = [int(sys.stdin.readline()) for _ in range(10)]
cnt_3 = 0
cnt_5 = 0
for i in range(len(lst)):
    if lst[i] % 3 == 0:
        cnt_3 += 1
    if lst[i] % 5 == 0:
        cnt_5 += 1

print(cnt_3,cnt_5)
