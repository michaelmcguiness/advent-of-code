def arrayManipulation(n, queries):
    starts = [(q[0], q[2]) for q in queries]
    ends = [(q[1], -q[2]) for q in queries]

    print(starts+ends)
    events = sorted(starts + ends, key=lambda x: (x[0], -x[1]))
    print(events)

    max_val = 0
    total = 0
    for idx, val in events:
        total += val
        max_val = max(total, max_val)
    return max_val


if __name__ == '__main__':
    fptr = open('array_manipulation_solution.txt', 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
