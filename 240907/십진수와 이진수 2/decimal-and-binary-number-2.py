n = input()


def toNum(binary):
    result = 0
    binary = binary[::-1]
    for i in range(len(binary)):
        result += (2 ** i) * int(binary[i])
    return result


def toBinary(num, jb):
    result = ''
    while (True):
        if num < jb:
            result += str(num % jb)
            break
        result += str(num % jb)
        num = num // jb
    return result[::-1]


print(toBinary(toNum(n) * 17, 2))