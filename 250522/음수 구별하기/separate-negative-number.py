import sys

n = int(sys.stdin.readline())
print(n)
def minusOrNot(n):
    return "" if n > 0 else "minus"

print(minusOrNot(n))