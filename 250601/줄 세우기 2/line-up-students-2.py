n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

# Please write your code here.
new_order = sorted(students, key= lambda x: (x[0], -x[1]))
for i in new_order:
    print(*i)