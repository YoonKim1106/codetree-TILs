total = 0
num = 0
while True:
    age = int(input())
    if 20 <= age < 30:
        total += age
        num += 1
    else:
        if num > 0:
           print(f'{total/num:.2f}') 
        break