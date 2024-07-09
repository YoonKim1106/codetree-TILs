a,b = map(int, input().split())

def count_number(a,b):
    count = 0
    for i in range(a,b+1):
        if i % 3 == 0:
            count += 1
        else:
            str_i = str(i)
            if '3' in str_i or '6' in str_i or '9' in str_i:
                count += 1
    return count


result = count_number(a,b)
print(result)