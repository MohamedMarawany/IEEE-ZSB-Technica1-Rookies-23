s1, s2 = input().split()

count = 0
flag = 0

for i in range(len(s2)):
    if(s1.count(s2[i])>0):
        count += 1
        if(count == len(s1)):
            flag = 1
            break
    else: count = 0

if(flag == 1):
    print("True")
else: print("False")
