max_len = 0
min_len = 20 
for _ in range(3):
    word = input()
    max_len = max(max_len, len(word))
    min_len = min(min_len, len(word))
print(max_len - min_len)