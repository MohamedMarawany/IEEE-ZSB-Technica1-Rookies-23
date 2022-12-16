#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    flag = None
    for i in range(p , q+1):
        n = str(i*i)
        l = n[:len(n)//2]
        r = n[len(n)//2:]
        if l == "":
            l = 0
        if int(l)+int(r) == i:
            flag = not None
            print(i, end=" ")
    if flag == None:
        print("INVALID RANGE")
    
if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
