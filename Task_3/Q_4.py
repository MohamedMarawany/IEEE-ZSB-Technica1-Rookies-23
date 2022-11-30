def minturn(N, P):
    if(N%2 == 0):
        N += 1
    
    return min((P+1)/2, (N-P+1)/2)

N = int(input("Enter Number of Pages: "))
P = int(input("Enter The Page Turn To: "))

print(int(minturn(N, P)))
