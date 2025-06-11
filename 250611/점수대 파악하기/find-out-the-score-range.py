import sys

lst = list(map(int, sys.stdin.readline().split()))

grade_count = sorted([i for i in range(10,110, 10)], reverse=True)
count = [0] * 10 
#print(grade_count)
#print(count)


for num in lst:
    if num == 0:
        break
    if 10 <= num  <= 100:
        tens = num  // 10
        if 1 <= tens <= 10:
            count[tens - 1] += 1
            
count = list(reversed(count))
for i in range(len(grade_count)):
    print(f"{grade_count[i]} - {count[i]}")