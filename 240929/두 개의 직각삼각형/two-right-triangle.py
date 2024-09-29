n = int(input())

for i in range(n):
    for k in range(n-i):
        print('*', end='')

    for j in range(2*i):
        print(' ', end='')
    
    for s in range(n-i):
        print('*', end='')
    print()