def collatz_count(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        count += 1
    return count

n = int(input())
print(collatz_count(n))
        
    


