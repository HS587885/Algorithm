string = input()
first = string[0]
second = string[1]

answer = []
for i in string:
    if i == second:
        answer.append(first)
    elif i == first:
        answer.append(second)
    else:
        answer.append(i)

print(''.join(answer))