# cook your dish here
for _ in range(int(input())) :
    for _ in range(int(input())) :
        I, N, Q = map(int, input().split())
        
        if I == Q :
            print( N//2 )
        elif I != Q :
            if N&1 :
                print( (N+1)//2 )
            else :
                print(N//2)