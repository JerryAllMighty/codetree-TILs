n = int(input())


def recursive(num):
    if num < 10:
        return num ** 2
    return (recursive(num // 10)) + (num % 10) ** 2


print(recursive(n))