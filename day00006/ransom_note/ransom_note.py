from collections import defaultdict

def convertToDict(strings):
    d = defaultdict(lambda: 0)
    for s in strings:
        d[s] += 1
    return d

def checkMagazine(magazine, note):
    m = convertToDict(magazine)
    n = convertToDict(note)

    for word, count in n.items():
        if m[word] < count:
            print("No")
            return

    print("Yes")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
