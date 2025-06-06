lst = list(map(int, input().split()))
total = sum([lst[i] for i in range(len(lst)) if (i + 1) % 2 == 0])
avg1 = [lst[i] for i in range(len(lst)) if (i + 1) % 3 == 0]
average = sum(avg1) / len(avg1)

print(total, round(average,1))