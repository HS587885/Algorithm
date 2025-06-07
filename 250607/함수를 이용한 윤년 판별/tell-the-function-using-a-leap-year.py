y = int(input())

#please write your code here.

def f(n):
    if n % 4 == 0:
        if n % 100 == 0 and n % 400 != 0:
            return "false"
        else:
            return "true"

 


print(f(y))

