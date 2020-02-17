try:
    n,q=map(int,input().split())
    a=[int(i) for i in input().split()][:n]
    a.sort()
    for k in range(q):
        c=-1
        i=int(input())
        if(i>=a[0]):
            s=0
            e=len(a)-1
            ans=-1
            while(s<=e):
                m=(s+e)//2
                if(a[m]<=i):
                    s=m+1
                else:
                    ans=m
                    e=m-1
            if(ans<0):
                print(a[-1])
                c=1
            else:
                print(a[ans-1])
                c=1 
        if(c==-1):
            print("-1")
except:
    pass
