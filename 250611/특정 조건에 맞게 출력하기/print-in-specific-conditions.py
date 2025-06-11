import sys

lst = list(map(int, sys.stdin.readline().split()))

answer = []
for i in range(len(lst)):

    if lst[i] == 0:
        print(*answer)
        break

    if lst[i] % 2 == 0:
        lst[i] //= 2
        answer.append(lst[i])
        
    else:
        lst[i] += 3
        answer.append(lst[i])
    
    