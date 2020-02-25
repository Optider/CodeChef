# cook your dish here
for _ in range(int(input())) :
    N = int(input())
    nums = list(map(int, input().split()))
    visited = {0:0, 1:0}
    for i in nums :
        if i%2 :
            visited[1] += 1
        else :
            visited[0] += 1
    print(visited[0]*visited[1])