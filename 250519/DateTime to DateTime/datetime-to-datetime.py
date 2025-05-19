import sys

a, b, c = map(int, sys.stdin.readline().split())

# Please write your code here.
start_minutes = (11 * 24 * 60) + (11 * 60) + 11

target_minutes = (a * 24 * 60) + (b * 60) + c

elapsed_time = target_minutes - start_minutes

# 결과 출력 (음수면 -1 출력)
print(elapsed_time if elapsed_time >= 0 else -1)
