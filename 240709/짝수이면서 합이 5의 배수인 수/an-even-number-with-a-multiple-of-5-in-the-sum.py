def check_number(N):
    tens = N //10
    units = N % 10

    sum_ = 0

    if ((tens + units) % 5 == 0 and units % 2 == 0):
        return "Yes"
    else:
        return "No"


N = int(input())

a = check_number(N)

print(a)