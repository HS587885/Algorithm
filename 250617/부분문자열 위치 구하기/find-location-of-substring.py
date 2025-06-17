def solve():
    input_str = input().strip()
    target_str = input().strip()
    
    # find() 함수는 부분 문자열이 존재하면 시작 인덱스를, 없으면 -1을 반환
    result = input_str.find(target_str)
    
    if result != -1:
        print(result)
    else:
        print(-1)  # 부분 문자열이 없는 경우

solve()
