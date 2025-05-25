import sys
a = int(sys.stdin.readline())
print("pass" if a >= 80 else f'{80-a} more score')