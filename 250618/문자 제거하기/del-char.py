s = list(input())  # 문자열 입력을 리스트로 변환

try:
    while len(s) > 1:
        idx = int(input())
        if idx >= len(s):
            s.pop()  # 마지막 문자 제거
        else:
            s.pop(idx)  # 해당 인덱스 문자 제거
        print("".join(s))  # 문자열로 변환 후 출력
except EOFError:
    pass  

