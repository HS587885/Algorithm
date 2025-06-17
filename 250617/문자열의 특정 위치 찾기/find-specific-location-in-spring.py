w, s= map(str, input().split())
idx = [i for i in range(len(w)) if w[i] == s]
print(idx[0] if idx != []  else "No")