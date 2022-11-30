from array import array
from cgi import print_form

def sum_arr(B):
    sum_1 = 0
    sum_2 = 0

    for i in range(len(B)):
        sum_1 += B[i][i]
        for j in range(len(B)):
            if (i+j) == (len(B)-1):
                sum_2 += B[i][j]

    sum_3 = sum_2 - sum_1

    return abs(sum_3)

A = int(input().strip())
B = []

for n in range(A):
    B.append(list(map(int, input().rstrip().split())))

print(B)

res = sum_arr(B)
print(res)
