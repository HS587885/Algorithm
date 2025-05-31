from collections import deque

n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

ad = deque(d)
at = deque(t)

bd = deque(d2)
bt = deque(t2)

a_status = 0
b_status = 0
time = 0

# 초기화
if ad:
    a_direction = ad.popleft()
    a_time = at.popleft()
else:
    a_direction = ''
    a_time = 0

if bd:
    b_direction = bd.popleft()
    b_time = bt.popleft()
else:
    b_direction = ''
    b_time = 0

while True:
    time += 1

    # A 이동
    if a_direction == "L":
        a_status -= 1
    elif a_direction == "R":
        a_status += 1
    a_time -= 1
    if a_time == 0:
        if ad:
            a_direction = ad.popleft()
            a_time = at.popleft()

    # B 이동
    if b_direction == "L":
        b_status -= 1
    elif b_direction == "R":
        b_status += 1
    b_time -= 1
    if b_time == 0:
        if bd:
            b_direction = bd.popleft()
            b_time = bt.popleft()

    if a_status == b_status:
        print(time)
        break

    # A, B 모두 이동 끝나면 종료
    if (not ad and a_time == 0) and (not bd and b_time == 0):
        print(-1)
        break
