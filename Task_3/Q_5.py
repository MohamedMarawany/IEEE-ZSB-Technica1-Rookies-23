import sys,math
n,m=map(int,sys.stdin.readline().split())
l=list(map(int,sys.stdin.readline().split()))
l=[x+1 for x in l]
print(l)
ans=-100000
for i in range(n):
    for j in range(m):
        ans=max(ans,abs(i-m))
print(ans)
