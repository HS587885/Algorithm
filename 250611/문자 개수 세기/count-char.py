word = input()
alphabet = input()

cnt = 0
for i in word:
    if i == alphabet:
        cnt += 1
print(cnt)
