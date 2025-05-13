n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def find_max(arr, n):
    if n == 1:
        return arr[0]
    max_rest = find_max(arr, n - 1)
    return max(arr[n - 1], max_rest)

# 사용 예시
print(find_max(arr, n))
