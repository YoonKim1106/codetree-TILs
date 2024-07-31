a,b = map(int, input().split())

def aaa(a,b):
    numbers = []
    for i in range(a,b+1):
        if i % 6 == 0 and i % 8 != 0:
            numbers.append(i)
    
    sum_num = 0

    for j in numbers:
        sum_num += j

    print(sum_num)


aaa(a,b)