def a(N):
    sum_ = 0
    for i in range(1,N+1):
        sum_ += i
    return (sum_ // 10)


N = int(input())

result = a(N)

print(result)