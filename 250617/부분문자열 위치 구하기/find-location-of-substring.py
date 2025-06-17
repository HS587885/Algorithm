input_str = input()
target_str = input()

# Please write your code here.
s = input_str
length = len(s)
cnt = 0

t1, t2 = target_str[0], target_str[1]
for i in range(length - 1):
    if s[i] == t1 and s[i + 1] == t2:
        cnt += 1


print(cnt if cnt > 0 else -1)        
