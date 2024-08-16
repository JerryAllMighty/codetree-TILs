n = int(input())


def recursive(num):
    if num == 1 or num == 2:
        return 1
    return recursive(num-1) + recursive(num-2)

print(recursive(n))