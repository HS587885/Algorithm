import sys

lst = [int(sys.stdin.readline()) for _ in range(10)]
filtered = [i for i in lst if 0<= i <= 200]
total = sum(filtered)
average = total / len(filtered)
print(total,("%.1f" % round(average, 1)) )
