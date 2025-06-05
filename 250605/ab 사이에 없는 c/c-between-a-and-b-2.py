a,b,c = map(int, input().split())
print("NO" if len([i for i in range(a,b+1) if i % c == 0]) > 0 else "YES")