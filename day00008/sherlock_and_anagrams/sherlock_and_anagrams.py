#!/bin/python3
import os
import math
from collections import defaultdict 

def dictOfSubstrings(s):
    d = defaultdict(lambda: 0)
    frameSize = len(s) - 1
    while frameSize > 0:
        for i in range(len(s) - frameSize + 1):
            # sort bc letters don't have to be in order for it to count
            substr = ''.join(sorted(s[i:i + frameSize]))
            d[substr] += 1
        frameSize -= 1
    return d

def combinations(n, r):
    return int(math.factorial(n)/(math.factorial(n - r) * math.factorial(r)))

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    substrDict = dictOfSubstrings(s)
    pairs = 0
    for substr, count in substrDict.items():
        # Combinations formula
        if count > 1:
            pairs += combinations(count, 2)
    print(substrDict)
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
