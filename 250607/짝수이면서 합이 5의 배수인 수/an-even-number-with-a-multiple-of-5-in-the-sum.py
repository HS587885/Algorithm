n = int(input())

# Please write your code here.
def f(n):
    str_num = str(n)
    added_num = int(str_num[1]) + int(str_num[0])
    if n % 2 == 0 and added_num % 5 == 0:
        return "Yes"
    
    return "No"

print(f(n))