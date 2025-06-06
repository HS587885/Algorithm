lst = list(map(int, input().split()))
odd = sum([lst[i] for i in range(len(lst)) if (i + 1) % 2 == 1])
even = sum([lst[i] for i in range(len(lst))if (i + 1) % 2 == 0])
print(odd - even if odd >= even else even - odd)