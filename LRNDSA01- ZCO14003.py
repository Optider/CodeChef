# cook your dish here
nums = []
length = int(input())

for _ in range(length) :
    nums.append(int(input()))

nums.sort()
max_prod = 0
for i, n in enumerate(nums) :
    
    prod = n * (length-i)
    if prod > max_prod :
        max_prod = prod
        
print(max_prod)