from decimal import Decimal, getcontext, ROUND_DOWN

A, B = map(int, input().split())

# 소수점 21자리까지 정확히 계산
getcontext().prec = 30  # 충분히 긴 자리수 확보
result = Decimal(A) / Decimal(B)

# 소수점 21번째 자리까지 내림 처리
truncated_result = result.quantize(Decimal('1.' + '0'*20), rounding=ROUND_DOWN)

print(truncated_result)
