math1 ,eng1 = map(int, input().split())
math2 ,eng2 = map(int, input().split())

print(1 if math1 > math2 and eng1 > eng2 else 0)