n = int(input())


def recursive(num):
    if num == 2:
        return 2
    elif num == 1:
        return 1

    if num % 2 == 0:
        return num + recursive(num - 2)
    else:
        return num + recursive(num - 2)


print(recursive(n))