lst = list(map(int, input().split()))


def isContinuous(targetList):
    if targetList[0] + 1 == targetList[1] and targetList[1] + 1 == targetList[2]:
        return True
    return False


def isAlmostContinuous(targetList):
    if ((targetList[0] + 2) == targetList[1]) or ((targetList[1]+2) == targetList[2]):
        return True
    return False

if isContinuous(lst):
    print(0)
elif isAlmostContinuous(lst):
    print(1)
else:
    print(2)