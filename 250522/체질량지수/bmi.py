h,w = map(int, input().split())
answer = (10000 * w) // (h ** 2)
print(answer)
print("Obesity" if answer >= 25 else "")
