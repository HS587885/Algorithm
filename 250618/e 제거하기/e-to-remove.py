word = list(input())

answer = []
cnt = 1
for i in range(len(word)):
    if word[i] == 'e' and cnt > 0:
        cnt -= 1
    else:
        answer.append(word[i])

print(''.join(answer))

