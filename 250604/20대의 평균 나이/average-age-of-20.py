total = 0
cnt = 0
while True:
    n = int(input())
    if n > 29:
        average = total / cnt
        print(("%.2f" % round(average, 2)))
        break

    else:
        total += n
        cnt += 1
