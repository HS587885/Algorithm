n = int(input())
sequence = [1, n]

while True:
    next_num = sequence[-1] + sequence[-2]
    sequence.append(next_num)

    if next_num > 100:
        break
    

print(' '.join(map(str, sequence)))
