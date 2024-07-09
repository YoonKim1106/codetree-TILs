def find_min(a,b,c):
    return min(a,b,c)


a,b,c = map(int, input().split())

min_val = find_min(a,b,c)
print(min_val)