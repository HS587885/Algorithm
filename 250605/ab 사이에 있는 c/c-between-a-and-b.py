a,b,c = map(int, input().split())

answer = len([i for i in range(a,b+1) if i % c == 0])
print("YES" if answer > 0 else "NO")