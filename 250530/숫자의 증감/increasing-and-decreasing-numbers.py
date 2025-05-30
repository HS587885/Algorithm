c, n = map(str, input().split())
n = int(n)

if c == 'A':
    i = 1
    while i <= n:
        print(i, end = ' ')
        i += 1
else:
    i = n
    while i > 0:
        print(i, end = ' ')
        i -= 1

    
