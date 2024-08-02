# 정수 a를 입력받습니다.
a = int(input().strip())

# 1부터 a까지의 수를 순회합니다.
result = []
for i in range(1, a + 1):
    # 조건을 모두 만족하지 않는 수를 찾습니다.
    if not (i % 2 == 0 and i % 4 != 0) and not (i // 8 % 2 == 0) and not (i % 7 < 4):
        result.append(i)

# 결과를 출력합니다.
print(" ".join(map(str, result)))