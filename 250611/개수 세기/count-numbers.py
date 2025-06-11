n,m = map(int, input().split())
lst = list(map(int, input().split()))

answer = len([i for i in lst if i == m])
print(answer)
