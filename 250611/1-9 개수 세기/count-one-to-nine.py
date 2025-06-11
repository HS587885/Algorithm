n = int(input())
numbers = list(map(int, input().split()))
# 1부터 9까지의 등장 횟수를 저장할 리스트 (index 0은 사용하지 않음)
count = [0] * 10

# 숫자 세기
for num in numbers:
    count[num] += 1

# 1부터 9까지 출력
for i in range(1, 10):
    print(count[i])
