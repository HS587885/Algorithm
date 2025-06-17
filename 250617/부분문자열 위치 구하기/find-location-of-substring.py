input_str = input()
target_str = input()

# Please write your code here.
result = input_str.replace(target_str, '#')
answer = result.count('#')
print(answer if answer != 0 else -1)