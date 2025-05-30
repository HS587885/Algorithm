b,a = map(int, input().split())

answer = sorted([i for i in range(a, b+1, 2)], reverse =True)
print(*answer)