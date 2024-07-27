person1_info = list(input().split())
person2_info = list(input().split())

person1_a = int(person1_info[0])
person2_a = int(person2_info[0])

person1_s = person1_info[1]
person2_s = person2_info[1]

def check(person1_a,person1_s,person2_a,person2_s):
    if (person1_a > 19 and person1_s == 'M') or (person2_a > 19 and person1_s == 'M'):
        print(1)
    else:
        print(0)

check(person1_a,person1_s,person2_a,person2_s)