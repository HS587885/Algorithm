from collections import deque

n = int(input())
cmd = []
num = []

for _ in range(n):
    line = input().split()
    cmd.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        num.append(int(line[1]))
    else:
        num.append(0)

# Please write your code here.
q = deque()

for i in range(len(cmd)):
    if cmd[i] == "push_front":
        q.appendleft(num[i])
    elif cmd[i] ==  "push_back":
        q.append(num[i])
    elif cmd[i] ==  "pop_front":
        pop_front = q.popleft()
        print(pop_front)
    elif cmd[i] ==  "pop_back":
        pop_back = q.pop()
        print(pop_back)
    elif cmd[i] ==  "size":
        print(len(q))
    elif cmd[i] ==  "empty":
        print(0 if q else 1)
    elif cmd[i] ==  "front":
        print(q[0])
    elif cmd[i] ==  "back":
        print(q[-1])


    