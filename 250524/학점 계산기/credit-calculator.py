import sys

n = int(sys.stdin.readline())

arr = list(map(float, sys.stdin.readline().split()))

def grading(score):
    if score >= 4.0:
        return "Perfect"
    elif 3.0 <= score < 4.0:
        return "Good"
    else:
        return "Poor"


average = sum(arr) / len(arr)
print(round(average, 1))
print(grading(average))