from collections import deque

N = int(input())

# 방문한 숫자는 다시 탐색하지 않도록 하기 위한 set
visited = set()

# 큐에 (현재 숫자, 연산 횟수)를 저장
q = deque()
q.append((N, 0))
visited.add(N)

while q:
    num, cnt = q.popleft()

    # 1에 도달했으면 정답 출력
    if num == 1:
        print(cnt)
        break

    # 다음 가능한 연산들을 조건에 따라 큐에 추가
    # 1. -1
    if num - 1 > 0 and (num - 1) not in visited:
        q.append((num - 1, cnt + 1))
        visited.add(num - 1)

    # 2. +1
    if (num + 1) not in visited:
        q.append((num + 1, cnt + 1))
        visited.add(num + 1)

    # 3. /2
    if num % 2 == 0 and (num // 2) not in visited:
        q.append((num // 2, cnt + 1))
        visited.add(num // 2)

    # 4. /3
    if num % 3 == 0 and (num // 3) not in visited:
        q.append((num // 3, cnt + 1))
        visited.add(num // 3)
