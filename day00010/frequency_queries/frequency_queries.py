#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.


def freqQuery(queries):
    vals = defaultdict(lambda: 0)
    freqs = defaultdict(lambda: 0)
    ans = []
    for x in queries:
        if (x[0] == 1):
            freqs[vals[x[1]]] -= 1
            vals[x[1]] += 1
            freqs[vals[x[1]]] += 1
        if (x[0] == 2):
            if (vals[x[1]] > 0):
                freqs[vals[x[1]]] -= 1
                vals[x[1]] -= 1
                freqs[vals[x[1]]] += 1
        if (x[0] == 3):
            if freqs[x[1]] > 0:
                ans.append(1)
            else:
                ans.append(0)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
