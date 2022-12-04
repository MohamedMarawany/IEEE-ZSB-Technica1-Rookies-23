n = int(input("Enter Number Of Words: "))
dic = {}

for i in range(n):
    A = input()
    B = "".join(sorted(A))
    if B in dic.keys():
        dic[B].append(A)
    else:
        dic[B] = []
        dic[B].append(A)

for res in dic.values():
    print(res)
    
