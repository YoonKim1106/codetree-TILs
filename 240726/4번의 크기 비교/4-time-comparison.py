a = int(input())

b,c,d,e = map(int, input().split())


def aaa(a,b,c,d,e):
    if a > b:
        print(1)
    else:
        print(0)

    if a > c:
        print(1)
    else:
        print(0)

    if a > d:
        print(1)
    else:
        print(0)

    if a > e:
        print(1)
    else:
        print(0)

aaa(a,b,c,d,e)