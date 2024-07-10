def is_prime(N):
    if N <= 1:
        return False
    for i in range(2,N):
        if N % i == 0:
            return False
    return True
    
def sum_prime(a,b):
    total = 0
    for N in range(a,b+1):
        if is_prime(N):
            total += N
    return total


    

a,b = map(int,input().split())

print(sum_prime(a,b))