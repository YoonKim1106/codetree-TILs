a,b,c = map(int,input().split())

def aaa(a,b,c):
    st = True
    for i in range(a,b+1):
        if i % c == 0:   # c의 배수가 있음
            st = False

    if st == False:
        return 'NO'
    else:
        return 'YES'


print(aaa(a,b,c))