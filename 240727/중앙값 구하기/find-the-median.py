a, b, c = map(int, input().split())

# 세 개의 숫자를 리스트로 만듭니다.
values = [a, b, c]

# 리스트를 정렬합니다.
values.sort()

# 중앙값을 출력합니다.
print(values[1])