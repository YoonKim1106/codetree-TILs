n = int(input())

grades = list(map(float, input().split()))

avg_grades = round((sum(grades) / n),1)

print(f'{avg_grades}')

if avg_grades >= 4.0:
    print("Perfect")
elif avg_grades >= 3.0:
    print("Good")
else:
    print("Poor")