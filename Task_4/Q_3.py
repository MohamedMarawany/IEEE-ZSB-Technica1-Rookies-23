a = list(map(int, input().split()))

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if(a[i] == a[j]):
            res = j-i

print(res)
