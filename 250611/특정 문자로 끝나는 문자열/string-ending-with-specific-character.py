import sys

word_lst = [sys.stdin.readline().strip() for _ in range(10)]
letter = sys.stdin.readline().strip()

answer = [word for word in word_lst if word.endswith(letter)]

if not answer:
    print("None")
else:
    print(*answer, sep='\n')
