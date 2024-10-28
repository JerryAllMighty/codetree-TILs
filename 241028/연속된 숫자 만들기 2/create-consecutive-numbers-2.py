lst = list(map(int, input().split()))


def isContinuous(targetList):
    minNum = min(targetList)
    if (minNum + 1 in targetList) and (minNum + 2 in targetList):
        return True
    return False


def isAlmostContinuous(targetList):
    if ((targetList[0] + 2) == targetList[1]) or ((targetList[1] + 2) == targetList[2]):
        return True
    return False


if isContinuous(lst):
    print(0)
elif isAlmostContinuous(lst):
    print(1)
else:
    print(2)