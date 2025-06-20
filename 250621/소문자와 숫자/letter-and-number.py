s = input()
result = ''.join(c.lower() for c in s if c.isalnum())
print(result)
