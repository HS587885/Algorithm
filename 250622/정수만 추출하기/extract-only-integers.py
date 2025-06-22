import sys 

input = sys.stdin.readline

a,b = map(str, input().split())
a = a.split(".")
b = b.split("%")
print(int(a[0]) + int(b[0]))