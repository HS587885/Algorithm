a, b = map(int, input().split())

# Please write your code here.

def f(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


cnt = 0
for i in range(a,b+1):
    lst = [int(i) for i in list(str(i))]
    added_num = sum(lst)
    if added_num % 2 == 0 and f(i):
        cnt += 1
print(cnt)