a, b = map(int, input().split())

# Please write your code here.


def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True 

answer = 0
for i in range(a,b+1):
    if prime(i) == True:
        answer += i
print(answer)

