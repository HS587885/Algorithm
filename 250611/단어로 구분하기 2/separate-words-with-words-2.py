import sys

word_lst = sys.stdin.readline().split(" ")

for i in range(1,len(word_lst), 2):
    print(word_lst[i-1])