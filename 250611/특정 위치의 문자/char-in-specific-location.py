word = ['L', 'E', 'B', 'R','O','S']

w = input()
#print(word.index(w) if w in word else None)


# 해당 문자를 찾지 못했다면 -1
idx = -1

# 문자 탐색
for i in range(len(word)):
    if word[i] == w:
        idx = i

# 문자가 존재하지 않는 경우
if idx == -1:
    print(None)
else:
    print(idx)


