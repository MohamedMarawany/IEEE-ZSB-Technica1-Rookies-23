import re


n, k = map(int, input().split())
a = list(map(int,input("\nEnter The Numbers : ").strip().split()))[:n]
b = list(set(a))

freq = []

for i in b:
    c = a.count(i)
    freq.append(c)

res = dict(zip(freq, b))

d = reversed(sorted(res))

ans = []
for i in d:
    ans.append(res[i])

print(ans[:k])
