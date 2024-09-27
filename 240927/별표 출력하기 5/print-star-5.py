n = int(input())

for i in range(n):
    stars = ('*' * (n - i) + ' ') * (n - i - 1) + '*' * (n - i)
    print(stars)