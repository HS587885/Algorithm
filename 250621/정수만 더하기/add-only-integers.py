s = input()
result = sum(int(c) for c in s if c.isnumeric())
print(result)
