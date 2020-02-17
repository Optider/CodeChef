# cook your dish here
N,Q = map(int,input().split())
lis = list(map(int,input().split()))
lis.sort()
for i in range(Q):
    s = int(input())
    left = 0
    right = len(lis)-1
    sol = -float("Inf")
    while(left<=right):
        mid = int((left+right)/2)
        if lis[mid]>s:
            right = mid - 1
            continue
        elif lis[mid]==s:
            sol = s
            break
        elif lis[mid]<s:
            if lis[mid]>sol:
                sol = lis[mid]
            left = mid + 1
    if sol==-float("Inf"):
        print(-1)
    else:
        print(sol)