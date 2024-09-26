def has_common_divisor(a,b):
    common_divisior = set()

    for i in range(1,1921):
        if 1920 % i == 0:
            common_divisior.add(i)
    
    for i in range(1,2881):
        if 2880 % i == 0 and i in common_divisior and a <= i <= b:
            return 1
    
    return 0


a,b = map(int, input().split())


print(has_common_divisor(a,b))