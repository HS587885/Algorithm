n = int(input())

lst = sum([i for i in range(1, n+1) if n % i == 0 and i != n])
print("P" if lst == n else "N")
