import sys

word_lst = sys.stdin.readline().split()

for i in range(len(word_lst)-1,-1,-1):
    print(word_lst[i])