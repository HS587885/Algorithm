import sys

input = sys.stdin.readline

a,b = map(str, input().split())

answer1 = 0
if ord(a) > ord(b):
    answer1 = ord(a) - ord(b) 
else:
    answer1 = ord(b)- ord(a)

answer2 = ord(a) + ord(b) 
print(answer2,answer1)