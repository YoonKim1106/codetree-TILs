def print_star_pattern(n):
    # 상단 삼각형 출력
    for i in range(n):
        spaces = ' ' * (2 * i)
        stars = '* ' * (2 * (n - i) - 1)
        print(f"{spaces}{stars.strip()}")
    
    # 하단 삼각형 출력
    for i in range(n-2, -1, -1):
        spaces = ' ' * (2 * i)
        stars = '* ' * (2 * (n - i) - 1)
        print(f"{spaces}{stars.strip()}")

# n 값을 입력받고 출력
n = int(input())
print_star_pattern(n)