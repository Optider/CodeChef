for _ in range(int(input())) :
    N = int(input())
    cur = list(map(int, input().split()))
    min_speed = cur[0]
    count = 1
    for i in range( 1, N ):
        if (cur[i] < min_speed) :
            min_speed = cur[i]
            count += 1 
    print(count)