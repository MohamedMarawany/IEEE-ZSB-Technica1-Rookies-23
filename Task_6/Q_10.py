def delete(n,k,t):
    temp=[]
    for i in t:
        while k and temp and temp[-1]<i:
            temp.pop()
            k-=1
        temp.append(i)
    print(" ".join(map(str,temp)))


for i in range(int(input())):

    n,k=map(int,input().split())

    t=map(int,input().split())

    delete(n,k,t)
