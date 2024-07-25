def cal(a, b):
    if a == b:
        return a + 10, b + 10

    min_num = min(a, b)
    max_num = max(a, b)

    if min_num == a:
        a += 10
    else:
        a *= 2

    if min_num == b:
        b += 10
    else:
        b *= 2

    return a, b

# 입력을 받아 a와 b에 저장
a, b = map(int, input().split())

# 함수 호출 후 결과 출력
result_a, result_b = cal(a, b)
print(result_a, result_b)