# cook your dish here
for _ in range(int(input())) :
    N = int(input())
    
    # find no of multiples of (each multiples of 5)
    multiple = 5
    zeroes = 0
    while N/multiple :
        zeroes += int(N/multiple)
        multiple *= 5
    print(zeroes)