a, b = map(int, input().split())
N = list(map(int, input()))


num = 0

for i in range(len(N)):
    num = num * a + N[i]

n = num

digits = []

while True:
    if n < b:
        digits.append(n)
        break

    digits.append(n % b)
    n //= b

# print binary number
for digit in digits[::-1]:
    print(digit, end="")