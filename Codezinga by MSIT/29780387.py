def search(a,b,n):
    l=0
    h=n-1
    f=-1
    while(l<=h):
        m=int((l+h)/2)
        if(a[m]==b):
            return a[m]
        elif(b<a[m]):
            h=m-1
        else:
            f=a[m]
            l=m+1
    return f

n,q=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
while(q!=0):
    q-=1
    b=int(input())
    print(search(a,b,n))