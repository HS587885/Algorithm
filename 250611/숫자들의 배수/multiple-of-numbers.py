import sys

n = int(input())

cnt = 0 
for i in range(1, 11):
    result = i * n
    print(result, end = ' ')
    if result % 5 == 0:
        cnt += 1

    if cnt == 2:
        break
