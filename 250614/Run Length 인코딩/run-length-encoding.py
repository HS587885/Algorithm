
A = input()
a = A
# Please write your code here.


prev_char = a[0]
count = 1

cnts = ''
for i in range(1, len(a)):
    if a[i] == prev_char:
        count += 1
    else:
        cnts += (prev_char + str(count))
        prev_char = a[i]
        count = 1

cnts += (prev_char + str(count))
print(len(cnts))
print(cnts)
