#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    newArr = a[:]
    for i in range(len(a)):
        newArr[i - d] = a[i]
    return newArr

if __name__ == '__main__':
    filename = 'left-rotation.txt'
    fptr = open(filename, 'w')

    # Sample Input
    # 5 4
    # 1 2 3 4 5

    # Sample Output
    # 5 1 2 3 4

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

