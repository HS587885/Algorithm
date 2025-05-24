n = int(input())
arr = [sum(list(map(int, input().split()))) // 4 for _ in range(n)]
cnt = 0
for i in arr:
    if i >= 60:
        cnt += 1
        print("pass")
    else:
        print("fail")

print(cnt)