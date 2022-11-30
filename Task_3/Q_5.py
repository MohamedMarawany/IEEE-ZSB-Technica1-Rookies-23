n,m = map(int, input().split())
L = list(map(int, input().split()))

ans = 0

for i in range(1, m):
    ans = max(abs(L[i-1]-L[i])/2, ans)
print(ans)
