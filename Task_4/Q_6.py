def modfied_num(n): 

    res = 0

    A = sorted(str(n))
    B = ''.join(A)

    while n != 6174:
        A = sorted(str(n))
        B = ''.join(A) 
        n_asc = int(B) 
        n_desc = B[::-1] 

        for x in range(len(n_desc),4):
            n_desc = n_desc + '0'
            x += 1
        n_desc = int(n_desc)

        res += 1
        n = n_desc - n_asc

    return res      
print(modfied_num(input()))
