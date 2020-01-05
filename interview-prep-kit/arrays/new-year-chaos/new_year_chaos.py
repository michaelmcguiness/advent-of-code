def minimumBribes(q):
    bribes = 0
    for i in range(len(q)):
        # check for invalid state
        if (q[i] - i > 3):
            print("Too chaotic")
            return 1
        # Briber can't get more than one position before number's original position
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1

    print(bribes)
    return 0


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
