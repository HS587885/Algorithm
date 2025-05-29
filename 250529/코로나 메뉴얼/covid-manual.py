lst = []
for _ in range(3):
    cold, temperature = map(str, input().split())
    temperature = int(temperature)
    lst.append([cold, temperature])
a = 0
b = 0
c = 0
d = 0
for i in lst:
    cold, temperature = i[0], i[1]
    if temperature >= 37 and cold is "Y":
        a += 1
    elif temperature >= 37 and cold is "N":
        b += 1
    elif temperature < 37 and cold is "Y":
        c += 1
    else:
        d += 1

if a >= 2:
    print("E")
else:
    print("N")
