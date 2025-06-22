import sys 

input = sys.stdin.readline

word1 = input()
word2 = input()

d1 = ''.join(c for c in word1 if c.isdigit())
d2 = ''.join(c for c in word2 if c.isdigit())

print(int(d1) + int(d2))


