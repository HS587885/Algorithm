a, b, c = map(int, input().split())

# Please write your code here.
def f(a,b,c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c

print(f(a,b,c))
