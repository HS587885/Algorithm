n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
answer = []
for i in range(2, len(arr)):
    check = arr[i-1] + arr[i-2]
    if arr[i] == check:
        for num in arr[i-2:i+1]:
            answer.append(num)

answer = list(set(answer))
print(len(answer))
