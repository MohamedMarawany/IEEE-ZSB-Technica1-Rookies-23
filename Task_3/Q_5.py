n,m=map(int,input().split())
station=list(map(int,input().split()))
ans=-100000
city=[i for i in range(n)]
# print(city,station)
for i in city:
    out=100000000000
    for j in station:
        out=min(out,abs(i-j))
    ans=max(out,ans)
print(ans)
