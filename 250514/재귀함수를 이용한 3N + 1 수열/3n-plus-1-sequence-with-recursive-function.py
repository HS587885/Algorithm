n = int(input())


def f(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + f(n // 2) 
    else:
        return 1 + f(3 * n + 1)

print(f(n))