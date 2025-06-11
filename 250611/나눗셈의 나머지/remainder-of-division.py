a,b = map(int, input().split())

lst = []
while a >= 1:
    a  = a // b
    remainder = a % b
    lst.append(remainder)
   

cnt = [lst.count(i) ** 2 for i in list(set(lst))]
print(sum(cnt))
    
