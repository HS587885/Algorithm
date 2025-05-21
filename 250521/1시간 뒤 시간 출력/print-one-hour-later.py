a = input()
lst = a.split(":")
lst[0] = str(int(lst[0]) + 1)
print(str(lst[0]) + ':' + str(lst[1]) )
