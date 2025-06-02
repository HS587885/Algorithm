a,b = map(int, input().split())
lst = [i for i in range(a,b+1) if i % 5 ==0 or i % 7 == 0]
total = sum(lst)
average = total / len(lst)
print(total, ("%.1f" % round(average, 1)))