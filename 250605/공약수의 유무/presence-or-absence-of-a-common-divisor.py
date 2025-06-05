a,b = map(int,input().split())
answer = [i for i in range(a,b+1) if 1920 % i == 0 and 2880 % i == 0]
print(1 if len(answer) > 0 else 0)