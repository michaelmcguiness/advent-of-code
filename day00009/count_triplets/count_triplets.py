#!/bin/python3
import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    seconds = defaultdict(int)
    thirds = defaultdict(int)

    count = 0
    for val in arr:
        count += thirds[val]
        thirds[val*r] += seconds[val]
        seconds[val*r] += 1
    return count  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
