a, b = input().split()
b = int(b)

for _ in range(b):
    x, y, z = input().split()
    x = int(x)
    
    if x == 1:  
        y, z = int(y), int(z)
        a = list(a)
        a[y-1], a[z-1] = a[z-1], a[y-1]
        a = ''.join(a)
    else:  
        result = []
        for ch in a:
            if ch == y:
                result.append(z)
            elif ch == z:
                result.append(z) 
            else:
                result.append(ch)
        a = ''.join(result)
    
    print(a)
