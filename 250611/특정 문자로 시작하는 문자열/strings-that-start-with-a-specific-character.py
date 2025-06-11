import sys

n = int(sys.stdin.readline().strip())
word_lst = [sys.stdin.readline().strip() for _ in range(n)]
letter = sys.stdin.readline().strip()

answer = [len(i) for i in word_lst if i.startswith(letter)]
cnt = len(answer)
average = sum(answer) / cnt
print(cnt, ("%.2f" % round(average, 2)))