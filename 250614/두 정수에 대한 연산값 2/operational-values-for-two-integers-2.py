a,b = map(int, input().split())

# Please write your code here.
def f(a,b):
    if a > b:
        a *= 2
        b += 10
    else:
        b *= 2
        a += 10
    

    return a,b

print(*f(a,b))
