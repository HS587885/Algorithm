n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
buy = price[0]
p_temp = 0
profit = 0
for i in range(1, len(price)):
    for j in range(i, len(price)):
        if buy < price[j]:
            p_temp = price[j] - buy
            profit = max(profit, p_temp)
        
    buy = price[i]
print(profit)
            
