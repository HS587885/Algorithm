lst = [int(input()) for _ in range(5)]
answer = len([i for i in lst if i % 2 == 0])
print(answer)