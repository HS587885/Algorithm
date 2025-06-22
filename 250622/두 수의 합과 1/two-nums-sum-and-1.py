import sys 
input = sys.stdin.readline

a,b = map(int, input().split())
result = str(a + b)
answer = [i for i in result if i == "1"]
print(len(answer))

