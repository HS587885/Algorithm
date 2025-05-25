import sys

a,b = map(int, sys.stdin.readline().split())
share, remainder = divmod(a,b)
print(f'{share}...{remainder}')