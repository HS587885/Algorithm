a,b = map(int, input().split())
answer = []
if a < b:
    answer.append(1)
else:
    answer.append(0)

if a == b:
    answer.append(1)
else:
    answer.append(0)

print(*answer)
