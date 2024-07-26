phone_num = list(input())

phone_num[4:8],phone_num[9:13] = phone_num[9:13] , phone_num[4:8]


for i in (phone_num):
    print(i, end = '')