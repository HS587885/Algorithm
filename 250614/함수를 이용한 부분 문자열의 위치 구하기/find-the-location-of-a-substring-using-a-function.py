import sys
input = sys.stdin.readline

text = input().strip()      # 개행 문자 제거
pattern = input().strip()   # 개행 문자 제거

found = False
for i in range(len(text) - len(pattern) + 1):
    if text[i:i+len(pattern)] == pattern:
        print(i)
        found = True
        break

if not found:
    print(-1)

        
