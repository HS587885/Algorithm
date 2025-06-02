import sys

n = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(n)]
total = sum(lst)
average = total / len(lst)
print(total,("%.1f" % round(average, 1)) )
