n = int(input())
add = 0
for i in range(1, 101):
    add += i
    if add > n:
        print(i)
        break
