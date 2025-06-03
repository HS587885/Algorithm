from math import prod
a,b = map(int, input().split())
answer = prod([i for i in range(a,b+1)])
print(answer)