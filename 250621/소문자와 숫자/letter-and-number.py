s = input()
only_alpha_upper = ''.join(c.lower() if c.isalpha() else c for c in s)
only_alpha_upper = only_alpha_upper.replace('.', '').replace('@','')
print(only_alpha_upper)