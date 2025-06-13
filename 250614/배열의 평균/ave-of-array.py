arr = [
    list(map(int, input().split()))
    for _ in range(2)
]

# 가로 평균
for i in range(2):
    row_avg = sum(arr[i]) / len(arr[i])
    print(row_avg, end = ' ')
print()
# 세로 평균  
for j in range(len(arr[0])):
    col_sum = 0
    for i in range(2):
        col_sum += arr[i][j]
    col_avg = col_sum / 2
    print(col_avg, end = ' ')
print()
# 전체 평균
total = 0
count = 0
for i in range(2):
    for j in range(len(arr[0])):
        total += arr[i][j]
        count += 1
total_avg = total / count
print(total_avg, end = ' ')

