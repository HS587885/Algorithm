n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

# Please write your code here.
distances = []
for idx, (x, y) in points:
    distance = abs(x) + abs(y)
    distances.append((distance, idx))

distances.sort()

for dist, idx in distances:
    print(idx+1)