a, b = input().split()
k = input()


def toNum(n, jb):
    result = 0
    n = n[::-1]
    for i in range(len(n)):
        result += int(n[i]) * (jb ** i)
    return result


def convert(n, jb):
    result = ''
    while (True):
        if n < jb:
            result += str(n % jb)
            break
        result += str(n % jb)
        n = n // jb
    return result[::-1]

print(convert(toNum(k, int(a)), int(b)))