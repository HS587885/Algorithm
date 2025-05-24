import sys

arr = list(map(int, sys.stdin.readline().split()))
lst = []
for i in arr:
    if i == 0:
        break
    else:
        lst.append(int(i))

total = sum(lst)
average = total / len(lst)
print(total, ("%.1f" % average))