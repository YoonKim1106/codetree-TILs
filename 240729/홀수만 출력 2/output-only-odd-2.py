b,a = map(int,input().split())


def desceding_num(a,b):
    nums = []

    for i in range(a,b+1):
        if i % 2 != 0:
            nums.append(i)
    
    nums.sort(reverse = True)

    print(" ".join(map(str, nums)))

desceding_num(a,b)