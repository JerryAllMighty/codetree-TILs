n = int(input())


def toBinary(num):
    result = ''
    while (True):
        if num < 2:
            result = result + str(num % 2)
            break
        result = result + str(num % 2)
        num = num // 2

    return result[::-1]

print(toBinary(n))