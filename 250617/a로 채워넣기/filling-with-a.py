w = list(input())
#print(w)
w[1], w[-2] = 'a', 'a'
print(''.join(w))