numbers = [int(input()) for _ in range(5)]

if all(num % 3 == 0 for num in numbers):
    print(1)
else:
    print(0)