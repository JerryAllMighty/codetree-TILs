n, b = map(int, input().split())


def convert(num, jb):
    result = ''
    while (True):
        if num < jb:
            result += str(num % jb)
            break
        result += str(num % jb)
        num = num // jb
    return result[::-1]


print(convert(n, b))