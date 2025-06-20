s = input()
lst = list(range(97, 123))  # [97, 98, ..., 122] → 'a' to 'z'

idx = lst.index(ord(s))  # 현재 문자의 인덱스
next_idx = (idx + 1) % 26  # 다음 인덱스 (z 다음엔 a로 순환)

print(chr(lst[next_idx]))
