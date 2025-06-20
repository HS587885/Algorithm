import sys
input = sys.stdin.readline

a, b = input().split()

for i in [a, b]:
    if i.isnumeric():
        print(chr(int(i)), end=' ')
    else:
        print(ord(i), end=' ')
