n = int(input())
lst = list(map(int, input().split()))
answer = [i ** 2 for i in lst]
print(*answer)