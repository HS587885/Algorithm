total = 0
count = 0

while True:
    age = int(input())

    if 20 <= age <= 29:
        total += age
        count += 1
    else:
        break

if count > 0:
    average = total / count
    print("%.2f" % average)
else:
    print("입력된 20대가 없습니다.")


