#!/bin/python3

n=int(input())
choc=list(map(int,input().split()))
d,m=input().split()
d=int(d)
m=int(m)
count=0
for i in range(0,n):
    sum=0
    j=i
    while(j<n and j<i+m):
        sum+=choc[j]
        j+=1
    if(sum==d):
        count+=1
print(count)
