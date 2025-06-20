import sys

input = sys.stdin.readline

a,b,c,d,e = map(int, input().split())

for i in [a,b,c,d,e]:
    print(chr(i), end = ' ')