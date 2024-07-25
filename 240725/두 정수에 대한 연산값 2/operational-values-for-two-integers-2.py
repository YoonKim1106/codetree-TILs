def cal(a, b):
    min_num = min(a, b)
    max_num = max(a, b)

    if min_num == a:
        a += 10
    else:
        a *= 2

    if min_num == b:
        b += 10
    else:
        b *= 2

    return a, b

a, b = map(int, input().split())

print(cal(a, b))