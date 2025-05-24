import sys

arr = list(map(int, sys.stdin.readline().split()))
lst = []
cnt = 0
for i in arr:
    if i == 0:
        break
    if i % 2 == 0:
        lst.append(i)
        cnt += 1

total = sum(lst)
print(cnt,total)