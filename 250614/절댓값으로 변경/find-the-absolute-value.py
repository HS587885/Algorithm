n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
print(*[abs(i) for i in arr])