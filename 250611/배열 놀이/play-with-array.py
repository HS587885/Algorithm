
n, q  = map(int, input().split())
lst = list(map(int, input().split()))

command_lst = [list(map(int, input().split())) for _ in range(q)]


for i in command_lst:
    if len(i) == 3:
        order, s, e = i[0], i[1], i[2]
        print(*[lst[i-1] for i in range(s, e+1)])
    else:
        order, c = i[0], i[1]
        if order == 1:
            print(lst[c-1])
        else:
            mini_one = len(lst)
            for i in range(len(lst)):
                if lst[i] == c:
                    mini_one = min(mini_one, i+1)
            if c not in lst:
                mini_one = 0
            print(mini_one)
    