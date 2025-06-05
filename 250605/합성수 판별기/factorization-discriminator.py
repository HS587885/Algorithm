n = int(input())

def discriminator(n):
    for i in range(2, n): 
        if n % i == 0:
            return "C"
    return "N"


print(discriminator(n))