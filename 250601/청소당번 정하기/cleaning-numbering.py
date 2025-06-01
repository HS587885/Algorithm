n = int(input())

a = 2
b = 3
c = 12
i = 0
a_total = 0
b_total = 0
c_total = 0

    
while i < n:
    i += 1
    if i % a == 0 and i % b != 0 and i % c != 0:
        a_total += 1
    if i % a != 0 and i % b == 0 and i % c != 0:
        b_total += 1
    if i % a == 0 and i % b == 0 and i % c != 0:
        b_total += 1
    if i % a == 0 and i % b == 0 and i % c == 0:
        c_total += 1

print(a_total,b_total,c_total)