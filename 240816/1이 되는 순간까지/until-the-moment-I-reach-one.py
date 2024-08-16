n = int(input())


def recursive(num):
    result = 1
    if num == 1:
        return 1
    if num % 2 == 0:
        result += recursive(num // 2)
    else:
        result += recursive(num // 3)
    return result


print(recursive(n)-1)