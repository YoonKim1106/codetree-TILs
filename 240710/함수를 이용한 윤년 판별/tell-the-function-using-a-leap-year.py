def is_leap_year(y):
    if y % 400 == 0:
        return "true"
    elif y % 100 == 0:
        return "false"
    elif y % 4 == 0:
        return "true"
    else:
        return "false"

y = int(input())
print(is_leap_year(y))