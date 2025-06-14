n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
idx = [m]
while m > 1:
    if m  % 2 == 0:
        m //= 2

    else:
        m -= 1
    idx.append(m)

total = 0
for i in idx:
    total += A[i-1]
print(total)
        