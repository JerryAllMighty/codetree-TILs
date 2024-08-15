year = int(input())


def isYoonYear(n):
    isYoon = False
    if n % 4 == 0 or (n % 100 == 0 and n % 400 != 0):
        isYoon = True
    return isYoon

print('true' if isYoonYear(year) else 'false')