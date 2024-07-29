a,b = map(int,input().split())

curr = a
nums = []

while curr <= b:
    if curr % 2 == 0:
        nums.append(curr)
    curr += 2

print(" ".join(map(str,nums)))