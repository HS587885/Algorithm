import sys

lst = list(map(int, sys.stdin.readline().split()))
for i in range(1, 7):
    print(f'{i} - {lst.count(i)}')