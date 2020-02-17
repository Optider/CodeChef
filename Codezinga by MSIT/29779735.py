# cook your dish here
from bisect import bisect as bs
n,q=map(int, input().split())
l=[int(x) for x in input().split()]
l.sort()
for i in range(q):
    n=int(input())
    k=bs(l,n)
    print(l[k-1] if k else -1)