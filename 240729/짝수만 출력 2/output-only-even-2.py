b,a = map(int,input().split())

curr = a
nums=[]


while curr <= b:
    if curr % 2 == 0:
        nums.append(curr)
    curr += 1
nums.sort(reverse=True)

print(" ".join(map(str,nums)))