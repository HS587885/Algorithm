arr = list(map(int, input().split()))
total  = 0

f = []
for i in arr:
    if i >= 250:
        break
    else:
        f.append(i)

total = sum(f)
average = total / len(f)
print(int(total),("%.1f" % round(average, 1)) )