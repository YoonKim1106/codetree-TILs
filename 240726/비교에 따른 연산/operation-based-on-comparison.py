a,b = map(int,input().split())

def aaa(a,b):
    if a > b:
        print(f'{a*b}')
    else:
        print(f'{b//a}')


aaa(a,b)