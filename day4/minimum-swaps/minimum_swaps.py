def minimumSwaps(arr):
    swaps = 0
    noSwaps = False
    while not noSwaps:
        noSwaps = True
        for i, ele in enumerate(arr):
            if i != ele - 1:
                noSwaps = False
                swaps += 1
                tmp = arr[ele - 1]
                arr[ele - 1] = arr[i]
                arr[i] = tmp
    return swaps


if __name__ == '__main__':
    fptr = open('min_swaps.txt', 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
