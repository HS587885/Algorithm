n = int(input())

for i in range(1, n + 1):
    cond1 = (i % 7)  < 4
    cond2 = (i // 8)  % 2 == 0
    cond3 = (i % 2 == 0 and i % 4 != 0)
    
    if cond1 or cond2 or cond3:
        continue
    else:
        print(i, end=' ')