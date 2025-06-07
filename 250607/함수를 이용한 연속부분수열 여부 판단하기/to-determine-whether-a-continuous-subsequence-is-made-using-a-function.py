n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def f(a,b):
    if len(a) > len(b):
        for i in range(len(b), len(a)):
            if a[i - len(b):i] == b:
                return "Yes"
        return "No"
    else:
        for i in range(len(a), len(b)):
             if b[i - len(a):i] == a:
                return "Yes"
        return "No"

print(f(a,b))