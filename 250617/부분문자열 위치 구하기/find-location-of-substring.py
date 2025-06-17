input_str = input()
target_str = input()

found = False
for i in range(len(input_str) - 1):
    if input_str[i:i+2] == target_str:
        print(i)
        found = True
        break

if not found:
    print(-1)
