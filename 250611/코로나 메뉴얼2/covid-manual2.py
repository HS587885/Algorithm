import sys

lst = [list(map(str, sys.stdin.readline().split())) for _ in range(3)]

a = 0
b = 0
c = 0
d = 0
for i in lst:
    sym, temp = i[0], int(i[1])
    if sym == "Y" and temp >= 37:
        a += 1
    elif sym == "N" and temp >= 37:
        b += 1
        pass
    elif sym == "Y" and temp <= 36:
        c += 1
    elif sym == "N" and temp <= 36:
        d += 1


if a >= 2:
    print(a,b,c,d,"E")
else:
    print(a,b,c,d)


