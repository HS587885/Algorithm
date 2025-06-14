given_str = input()
n = int(input())


n = min(n, len(given_str))
length = len(given_str)
answer = ''
for i in range(length -1, length - n -1,-1):
    answer += given_str[i]
print(answer)
