# 입력받은 값을 공백을 기준으로 나눈 후 정수로 변환하여 리스트로 저장
numbers = list(map(int, input().split()))

# 0이 입력된 위치를 찾고 그 위치 이전까지의 값을 가져옴
if 0 in numbers:
    numbers = numbers[:numbers.index(0)]

# 역순으로 출력
print(" ".join(map(str, numbers[::-1])))
