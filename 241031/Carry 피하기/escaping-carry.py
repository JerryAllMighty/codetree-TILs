import itertools

cnt = int(input())
lst = []
maxLen = 0
for _ in range(cnt):
    val = input()
    lst.append(val)
    if len(val) > maxLen:
        maxLen = len(val)
cmp = []


def makeSameJaritsu():
    for i in lst:
        if len(i) != maxLen:
            gap = maxLen - len(i)
            cmp.append((gap * '0') + i)


def isCarry(targetString, targetCnt):
    targetList = targetString.split(' ')
    result = False
    for i in range(targetCnt - 1,-1,-1):
        if sum([int(j[i]) for j in targetList]) > 9:
            result = True
    return result


makeSameJaritsu()
answer = 0
for i in range(cnt - 1, -1, -1):
    permutationList = list(map(" ".join, itertools.permutations(cmp, i)))
    for j in permutationList:
        if isCarry(j, i) is False:
            print(i)
            exit(0)