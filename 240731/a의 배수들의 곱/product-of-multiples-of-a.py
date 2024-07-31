a,b = map(int,input().split())

def aaa(a,b):
    numbers = []
    for i in range(1,b+1):
        if i % a == 0:
            numbers.append(i)
        
    mul_num = 1

    for j in numbers:
        mul_num *= j
    
    print(mul_num)

aaa(a,b)