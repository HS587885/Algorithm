n = int(input())
arr = list(map(int, input().split()))

import math
# Please write your code here.
def lcm(a, b):
    return a * b // math.gcd(a, b)

def lcm_list(arr, idx=0):
    if idx == len(arr) - 1:
        return arr[idx]
    return lcm(arr[idx], lcm_list(arr, idx + 1))
print(lcm_list(arr))
