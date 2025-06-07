M, D = map(int, input().split())

# Please write your code here.
def f(m,d):
    if m < 0 or m > 12:
        return "No"
    days_in_month_2021 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return "Yes" if d <= days_in_month_2021[m-1] else "No"


print(f(M,D))
