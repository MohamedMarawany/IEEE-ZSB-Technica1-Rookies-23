A = 'hello'
B = input()

i = 0
j = 0

while i < len(A) and j < len(B):
    if A[i] == B[j]:
        i += 1
    j += 1
if i == len(A):
    print("YES")
else :
    print("NO")
