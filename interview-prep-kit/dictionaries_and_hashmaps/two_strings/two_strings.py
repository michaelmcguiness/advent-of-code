#!/bin/python3
import os
from collections import defaultdict


def convertToDict(string):
    d = defaultdict(lambda: 0)
    for c in string:
        d[c] += 1
    return d


def twoStrings(s1, s2):
    s1Dict = convertToDict(s1)
    s2Dict = convertToDict(s2)

    # just need to match one letter
    for c, count in s1Dict.items():
        if (s2Dict[c] > 0):
            return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
