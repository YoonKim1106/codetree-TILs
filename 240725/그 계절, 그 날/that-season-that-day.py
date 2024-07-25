y,m,d = map(int, input().split())



def is_leap_y(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def day_num_check(y,m):
    if m == 2:
        if is_leap_y(y):
            return 29
        else:
            return 28
    elif m in [4,6,9,11]:
        return 30
    else:
        return 31

def get_season(y,m,d):
    if m < 1 or m > 12:
        return -1
    days_in_m = day_num_check(y,m)
    if d < 1 or d > days_in_m:
        return -1
    if m in [3,4,5]:
        return "Spring"
    elif m in [6,7,8]:
        return "Summer"
    elif m in [9,10,11]:
        return "Fall"
    elif m in [12,1,2]:
        return "Winter"


print(get_season(y,m,d))