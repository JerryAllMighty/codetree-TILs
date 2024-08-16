n = int(input())


def recursive(num):
    if num == 1:
        return 1
    if num % 2 == 0:
        return 1 + recursive(num // 2)
    else:
        return 1 + recursive((num * 3) + 1)


print(recursive(n) - 1)