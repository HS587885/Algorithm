word = input().strip()

answer1 = ''
answer2 = ''

if 'ee' in word:
    answer1 = 'Yes'
else:
    answer1 = 'No'

if 'ab' in word:
    answer2 = 'Yes'
else:
    answer2 = 'No' 

print(answer1,answer2)