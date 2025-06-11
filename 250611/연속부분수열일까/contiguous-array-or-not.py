n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def f(a,b):
    for i in range(1, len(a)):
        prev = a[i - 1]
        curr = a[i]
        if prev == b[0] and curr == b[1]:
            return "Yes"
    return "No"

print(f(a,b))
