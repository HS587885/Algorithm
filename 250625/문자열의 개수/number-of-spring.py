import sys

input = sys.stdin.readline

cnt = 0
answer = []
for i in range(1, 201):
    word = input().strip()
    cnt += 1
    if word == "0":
        break
    
    if i % 2 != 0:
        answer.append(word)

print(cnt -1)
for i in answer:
    print(i)
