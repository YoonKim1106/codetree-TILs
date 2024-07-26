a = int(input())

values = list(map(int, input().split()))


def aaa(a, values):
    for i in values:
        if a > i:
            print(1)
        else:
            print(0)

aaa(a,values)