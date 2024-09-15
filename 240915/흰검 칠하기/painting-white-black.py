import collections

n = int(input())
givenLst = []
for _ in range(n):
    givenLst.append(input().split())

lst = [
    'L0R0C' for _ in range(100 * n)
]
current = 0


def findRLCount(targetString, direction):
    lIdx = targetString.index('L')
    rIdx = targetString.index('R')

    if direction == 'R':
        return int(targetString[rIdx+1:-1])
    elif direction == 'L':
        return int(targetString[lIdx+1:rIdx])


def findRLString(targetString, direction):
    rIdx = targetString.index('R')

    if direction == 'R':
        return targetString[:rIdx+1]
    elif direction == 'L':
        return targetString[rIdx:-1]


def colorTile(targetString, direction):
    lIdx = targetString.index('L')
    rIdx = targetString.index('R')

    if int(targetString[lIdx+1:rIdx]) >= 2 and int(targetString[rIdx+1:]) >= 2:
        return 'G'
    else:
        if direction == 'R':
            return 'B'
        elif direction == 'L':
            return 'W'


for i in givenLst:
    cnt, direction = int(i[0]), i[1]
    while (cnt > 0):
        if direction == 'R':
            rCnt = findRLCount(lst[current], 'R')
            lst[current] = findRLString(lst[current], 'R') + str(rCnt + 1)
            color = colorTile(lst[current], direction)
            lst[current] += color
            current += 1
        elif direction == 'L':
            lCnt = findRLCount(lst[current], 'L')
            lst[current] = 'L' + str(lCnt + 1) + findRLString(lst[current], 'L')
            color = colorTile(lst[current], direction)
            lst[current] += color
            current -= 1
        cnt -= 1
    if direction == 'R':
        current -= 1
    else:
        current += 1
w = 0
b = 0
g = 0
for key, val in collections.Counter(lst).items():
    if key[4] == 'W':
        w += val
    elif key[4] == 'B':
        b += val
    if key[4] == 'G':
        g += val

print(w, b, g)