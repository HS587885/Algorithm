import sys

lst = list(map(int, sys.stdin.readline().split()))
# 배열에 주어진 수를 입력받아 저장
count_arr = [0] * 7
	
for elem in lst:
	count_arr[elem] += 1
	
for i in range(1, 7):
	print(f"{i} - {count_arr[i]}")

