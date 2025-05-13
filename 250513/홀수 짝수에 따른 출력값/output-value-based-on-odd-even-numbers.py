N = int(input())

# Please write your code here.
def odd_even_separate_sum(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    elif n % 2 == 0:
        return n + odd_even_separate_sum(n-2)
    else:
        return n + odd_even_separate_sum(n-2)

print(odd_even_separate_sum(N))