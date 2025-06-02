n = int(input())
integers = [int(input()) for _ in range(n)]
answer = sum([i for i in integers if i % 2 != 0 and i % 3 == 0])
print(answer)
