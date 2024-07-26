# 물건과 가격 목록
items = {
    "book": 3000,
    "mask": 1000,
    "pen" : 500
}

# 사용자의 입력을 받습니다.
n = int(input().strip())

# 살 수 있는 물건 중 가장 비싼 것을 찾습니다.
max_item = None
for item, price in items.items():
    if price <= n:
        if max_item is None or price > items[max_item]:
            max_item = item

# 결과를 출력합니다.
if max_item:
    print(max_item)
else:
    print("no")