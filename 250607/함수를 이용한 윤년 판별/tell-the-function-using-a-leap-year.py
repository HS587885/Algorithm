y = int(input())

def f(n):
    if n % 4 == 0 and (n % 100 != 0 or n % 400 == 0):
        return "true"
    else:
        return "false"

print(f(y))


 



