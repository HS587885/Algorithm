binary = input()

# Please write your code here.
binary = list(map(int, binary))
num = 0

for i in range(len(binary)):
    num = num * 2 + binary[i]

print(num)