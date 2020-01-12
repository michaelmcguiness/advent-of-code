#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.


def countSwaps(a):
    total_swaps = 0
    swaps = 1
    while not swaps == 0:
        swaps = 0
        for i in range(len(a) - 1):
            if (a[i] > a[i + 1]):
                tmp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = tmp
                swaps += 1
        total_swaps += swaps
    print(f"Array is sorted in {total_swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
