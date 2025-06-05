lst = [int(input()) for _ in range(5)]
def f(lst):
    for i in lst:
        if i % 3 != 0:
            return 0
    return 1

print(f(lst))