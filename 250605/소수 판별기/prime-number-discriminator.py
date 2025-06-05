n = int(input())

def discriminator(n):
    answer = [i for i in range(1,n) if n % i == 0]
    if len(answer) > 2:
        return "C"
    else:
        return "P"

print(discriminator(n))