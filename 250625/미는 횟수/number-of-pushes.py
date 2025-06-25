a = input()
b = input()

cnt = 0
original = a

for _ in range(len(a)):
    if a == b:
        print(cnt)
        break
    a = a[-1] + a[:-1]
    cnt += 1
else:
    print(-1)
