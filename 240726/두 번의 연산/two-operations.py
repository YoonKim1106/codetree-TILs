a = int(input())


def aaa(a):
    if a % 2 != 0:
        a += 3
    
    if a % 3 == 0:
        a  /= 3
    
    return int(a)


print(aaa(a))