a, b = map(int, input().split())

# 나머지 등장 횟수를 저장할 리스트
mod_list = [0] * b

while a > 1:
    idx = a % b
    mod_list[idx] += 1
    a //= b

# 등장 횟수의 제곱을 모두 더함
ans = sum(x * x for x in mod_list)
print(ans)

