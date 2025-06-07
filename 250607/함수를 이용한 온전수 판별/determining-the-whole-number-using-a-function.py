import sys
a, b = map(int, sys.stdin.readline().split())

# Please write your code here.
def is_onjeonsu(n):
    if n % 2 == 0:
        return False
    if n % 10 == 5:
        return False
    if n % 3 == 0 and n % 9 != 0:
        return False
    return True

print(len([i for i in range(a,b+1) if is_onjeonsu(i) == True]))