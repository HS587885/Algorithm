import sys
input = sys.stdin.readline

N = int(input())
words = input().split()
joined = ''.join(words)

for i in range(0, len(joined), 5):
    print(joined[i:i+5])
