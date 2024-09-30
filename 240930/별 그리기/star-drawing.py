def draw_diamond(n):
    # 상단 부분 출력
    for i in range(n):
        spaces = ' ' * (n - i - 1)  # 공백의 개수
        stars = '*' * (2 * i + 1)   # 별의 개수
        print(f"{spaces}{stars}")

    # 하단 부분 출력
    for i in range(n - 2, -1, -1):
        spaces = ' ' * (n - i - 1)  # 공백의 개수
        stars = '*' * (2 * i + 1)   # 별의 개수
        print(f"{spaces}{stars}")

# n 입력받기
n = int(input())
draw_diamond(n)