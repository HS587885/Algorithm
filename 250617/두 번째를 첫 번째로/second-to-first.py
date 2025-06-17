word = list(input())

second_string = word[1]
first_string = word[0]

answer = [first_string if word[i] == second_string else word[i] for i in range(len(word)) ]
print(''.join(answer))