n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.


def f(a, b):
    if len(b) > len(a):
        return "No"
    
    for i in range(len(a) - len(b) + 1):
        if a[i:i+len(b)] == b:
            return "Yes"
    
    return "No"

print(f(a, b))
