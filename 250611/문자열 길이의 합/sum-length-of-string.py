n = int(input())
length = 0
cnt = 0
for _ in range(n):
    word = input()
    length += len(word)
    if word[0] == 'a':
        cnt += 1

print(length, cnt)

