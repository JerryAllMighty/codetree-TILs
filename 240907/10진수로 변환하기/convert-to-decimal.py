n = input()


def toNum(binary):
    result = 0
    binary = binary[::-1]
    for i in range(len(binary)):
        result += int(binary[i]) * (2 ** i)
    return result



print(toNum(n))