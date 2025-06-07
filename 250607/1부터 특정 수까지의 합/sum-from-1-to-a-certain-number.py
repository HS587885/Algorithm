n = int(input())

# Please write your code here.
def f(n):
    total = 0
    for i in range(1, n+1):
        total += i
    answer = total // 10
    return answer

print(f(n))