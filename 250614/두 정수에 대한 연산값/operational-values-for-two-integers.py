import sys

input = sys.stdin.readline

a, b = map(int, input().split())

# Please write your code here.
def f(a,b):
    if a > b:
        a += 25
    else:
        b += 25
    
    if a < b:
        a *= 2
    else:
        b *= 2
    return a,b

print(*f(a,b))