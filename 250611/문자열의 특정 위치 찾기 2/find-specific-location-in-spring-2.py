f = ["apple", "banana",
"grape", "blueberry",
"orange"]

letter = input()
answer = []
for i in range(len(f)):
    check = f[i]
    if check[2] == letter or check[3] == letter:
        answer.append(check)

for w in answer:
    print(w)
    
print(len(answer))