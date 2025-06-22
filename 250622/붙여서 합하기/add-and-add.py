import sys 

input = sys.stdin.readline
a,b = map(str, input().split())
ab = a + b
ba = b + a
print(int(ab) + int(ba))