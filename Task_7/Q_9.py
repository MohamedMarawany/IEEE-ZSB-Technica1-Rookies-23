def DistinctDigit(A):
 
    for i in range(A + 1, 9999):
        s = str(i)
        uniDigits = set([char for char in s])
        if (len(s) == len(uniDigits)):
            print(i)
            break
 
A = int(input())
B = str(A)
     
DistinctDigit(A)
