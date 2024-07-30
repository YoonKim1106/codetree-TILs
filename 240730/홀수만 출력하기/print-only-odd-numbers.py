N = int(input())
numbers= [int(input()) for _ in range(N)]

for i in numbers:
    if i % 2 != 0 and i % 3 == 0:
        print(i)