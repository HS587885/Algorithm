A = input()
B = input()

while B in A:
    idx = A.find(B)  # 가장 먼저 등장하는 위치
    A = A[:idx] + A[idx+len(B):]  # 해당 부분 제거

print(A)
