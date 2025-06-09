n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# A의 초별 누적 거리 기록
a_dist = []
cur = 0
for vi, ti in zip(v, t):
    for _ in range(ti):
        cur += vi
        a_dist.append(cur)

# B의 초별 누적 거리 기록
b_dist = []
cur = 0
for vi, ti in zip(v2, t2):
    for _ in range(ti):
        cur += vi
        b_dist.append(cur)

# 선두 변경 횟수 계산
cnt = 0
prev = None

for a, b in zip(a_dist, b_dist):
    if a > b:
        now = 'A'
    elif b > a:
        now = 'B'
    else:
        now = 'SAME'

    if prev is not None and now != prev and now != 'SAME':
        cnt += 1

    if now != 'SAME':
        prev = now

print(cnt)
