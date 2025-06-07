a, b = map(int, input().split())

# Please write your code here.
def check(n):
    str_num_lst = list(str(n))
    if "3" in str_num_lst or "6" in str_num_lst or "9" in str_num_lst:
        return True
    return False

def f(a,b):
    cnt = 0
    for i in range(a,b+1):
        if i % 3 == 0 or check(i) == True:
            cnt += 1
    return cnt

print(f(a,b))

