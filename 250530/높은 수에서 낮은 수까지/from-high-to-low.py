a, b = map(int, input().split())
answer = [i for i in range(b,a-1, -1)]
print(*answer)