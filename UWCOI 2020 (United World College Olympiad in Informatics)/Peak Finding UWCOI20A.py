# cook your dish here
for _ in range(int(input())) :
    nums = []
    cur_max = 0
    for i in range(int(input())) :
        nums.append(int(input()))
        if nums[-1] > cur_max :
            cur_max = nums[-1]
    print(cur_max)