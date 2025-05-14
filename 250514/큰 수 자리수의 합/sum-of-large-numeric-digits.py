a, b, c = map(int, input().split())

# Please write your code here.
number = a * b * c

def f(number):
    if number < 10:
        return number
    return f(number // 10) + (number % 10)
print(f(number))