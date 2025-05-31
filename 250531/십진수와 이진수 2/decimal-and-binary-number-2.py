N = input()

# Please write your code here.
N = list(map(int, N))
num = 0

for i in range(len(N)):
    num = num * 2 + N[i]

num *= 17
n = num

digits = []

while True:
    if n < 2:
        digits.append(n)
        break

    digits.append(n % 2)
    n //= 2

# print binary number
for digit in digits[::-1]:
    print(digit, end="")
