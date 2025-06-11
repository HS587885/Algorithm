import sys

a, b = map(int, sys.stdin.readline().split())
sequence = [a, b]

while len(sequence) < 10:
    next_num = sequence[-1] + (2 * sequence[-2])
    sequence.append(next_num)

print(' '.join(map(str, sequence)))
