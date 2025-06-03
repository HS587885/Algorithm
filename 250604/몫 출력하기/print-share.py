import sys
cnt = 3
while cnt > 0:
    n = int(sys.stdin.readline())
    if n % 2 == 0:
        n //= 2
        cnt -= 1
        print(n)
    else:
        pass

