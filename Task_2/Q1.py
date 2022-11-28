import random
from tokenize import Number
A = random.randint(100,1000)
B = str(A)
print(A)
hit = 0
miss = 0

while(True):
    C = input("Enter a Number ")
    for i in range(len(C)):
        if B[i] == C[i]:
            hit += 1
        elif C[i] in B :
            miss += 1
    if hit == 3:
        print("Number is True ")
        break
    print(hit, "hit", miss, "miss")
    hit = 0
    miss = 0
