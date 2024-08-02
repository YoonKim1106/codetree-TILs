n = int(input())

cnt = 0
div = 0
    
while n > 1:
    div += 1
    n //= div
    cnt += 1

print(cnt)