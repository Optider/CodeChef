import sys
import math
import copy
from itertools import permutations as pm
input=sys.stdin.readline
d={}

t=1
while t>0:
    t-=1
    n,m=map(int,input().split())
    a=[int(x) for x in input().split()]
    a.sort()
    for i in range(m):
        s=0
        x=int(input())
        e=n
        ans=-1
        while s<e:
            mid=(s+e)//2
            if a[mid]<=x:
                ans=a[mid]
                s=mid+1
            else:
                e=mid
            #print(s,e)    
        print(ans)    