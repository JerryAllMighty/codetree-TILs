n = int(input())


def recursive(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    return recursive(num // 3) + recursive(num - 1)


print(recursive(n))