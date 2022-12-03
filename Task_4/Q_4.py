n = int(input("Enter N Numbers: "))
a = list(map(int, input().split()))

flag = 1

while n>=1:
    if a[n-1] >= 9:
        flag = 0
        a[n-1] = 0
        a[n-2] += 1
        if a[0] > 9:
            a[0] = 0
            a.insert(0, 1)
    elif flag:
        a[n-1] += 1
        break
    n -= 1

print(a)
