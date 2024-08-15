year = int(input())


def isYoonYear(n):
    isYoon = False
    if n % 4 == 0:
        if n % 100 == 0 and n % 400 != 0:
            isYoon = False
        else:
            isYoon = True
    return isYoon

print('true' if isYoonYear(year) else 'false')