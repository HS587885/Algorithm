a,b = map(int, input().split())

# 수열 초기화
sequence = [a, b]

# 10개 될 때까지 반복
while len(sequence) < 10:
    next_digit = (sequence[-1] + sequence[-2]) % 10  # 합의 1의 자리
    sequence.append(next_digit)

# 출력
print(' '.join(map(str, sequence)))
