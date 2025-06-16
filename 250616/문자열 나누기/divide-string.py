import sys
input = sys.stdin.readline

N = int(input())
word = input().strip().replace(" ", "")
for i in range(5, len(word), 5):
    print(word[i-5:i])
print(word[-1])



