a,b = map(int, input().split())

   
lst = []
while a > 0:
    remainder = a % b
    lst.append(remainder)
    a = a // b

cnt = [lst.count(i) ** 2 for i in list(set(lst))]
print(sum(cnt))
    
