score = int(input())

def grading(n):
    if 90 <= n:
        return "A"
    elif 80 <= n < 90:
        return "B"
    elif 70 <= n < 80:
        return "C"
    elif 60 <= n < 70:
        return "D"
    elif 60 < n:
        return "F"


print(grading(score))