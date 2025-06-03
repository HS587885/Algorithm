n = int(input())

for i in range(1, n + 1):
    cond1 = (i % 2 == 0)
    cond2 = (i % 10 == 5)
    cond3 = (i % 3 == 0 and i % 9 != 0)
    
    if cond1 or cond2 or cond3:
        continue
    else:
        print(i, end=' ')



