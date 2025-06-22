import sys 

input = sys.stdin.readline

def extract_number(s):
    result = ''
    for c in s:
        if c.isdigit():
            result += c
        else:
            break
    return int(result)

a, b = input().split()

num1 = extract_number(a)
num2 = extract_number(b)

print(num1 + num2)
