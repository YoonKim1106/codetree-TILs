count = 0

while count < 3:
    num = int(input())
    if num % 2 == 0:
        print(num // 2)
        count += 1
    else:
        continue