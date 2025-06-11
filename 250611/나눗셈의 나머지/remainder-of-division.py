a, b = map(int, input().split())

remainders = []
while a > 0:
    remainder = a % b
    remainders.append(remainder)
    a = a // b

total = sum(remainders.count(i) ** 2 for i in set(remainders))
print(total)
