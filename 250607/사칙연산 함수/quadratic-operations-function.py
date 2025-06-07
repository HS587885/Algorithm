import sys


a, o, c = sys.stdin.readline().split()
a = int(a)
c = int(c)

# Please write your code here.
def f(a,o,c):
    if o == '*':
        return f'{a} * {c} = {a * c}' 
    elif o == '/':
        return f'{a} / {c} = {a / c}' 
    elif o == '-':
        return f'{a} - {c} = {a - c}' 
    elif 0 == '+':
        return f'{a} + {c} = {a + c}' 
    else:
        return False

print(f(a,o,c))