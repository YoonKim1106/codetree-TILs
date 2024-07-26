from statistics import mean
a,b,c = map(int,input().split())

mean_abc = mean([a,b,c])
sum_abc = a+b+c

print(f'{sum_abc}')
print(f'{mean_abc}')
print(f'{sum_abc - mean_abc}')