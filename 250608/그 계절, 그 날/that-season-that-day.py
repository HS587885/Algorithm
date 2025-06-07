Y, M, D = map(int, input().split())

# Please write your code here.
def leap_year(n):
    if n % 4 == 0 and (n % 100 != 0 or n % 400 == 0):
        return True
    else:
        return False

def season(m):
    if 3 <= m <= 5:
        return "Spring"
    elif 6 <= m <= 8:
        return "Summer"
    elif 9 <= m <= 11:
        return "Fall"
    else:
        return "Winter"


def function(y,m,d):
    if m < 0 or m > 12:
        return -1

    if leap_year(y) == False:
        days_in_month_leapYear = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return season(m) if d <= days_in_month_leapYear[m-1] else -1
    else:
        days_in_month_Year = days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return season(m) if d <= days_in_month_Year[m-1] else -1

print(function(Y,M,D))
 


    

    