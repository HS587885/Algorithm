word = input()
answer = [word[i] for i in range(len(word)) if i != 1 and i != len(word)-2]
print(''.join(answer))