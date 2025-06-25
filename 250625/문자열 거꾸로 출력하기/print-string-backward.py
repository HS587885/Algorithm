import sys

input = sys.stdin.readline

for _ in range(10):
    word = input().strip()
    if word == "END":
        break
    else:
        print(word[::-1])
