#!/bin/python3

# Complete the hourglassSum function below.


def hourglassSum(arr):
    largest = float("-inf")
    for y in range(len(arr) - 2):
        for x in range(len(arr[0]) - 2):
            glassSum = (arr[y][x] + arr[y][x + 1] + arr[y][x + 2] + arr[y + 1]
                        [x + 1] + arr[y + 2][x] + arr[y + 2][x + 1] + arr[y + 2][x + 2])
            if glassSum > largest:
                largest = glassSum
    return largest


if __name__ == '__main__':
    fptr = open('2d_array_solution.txt', 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
