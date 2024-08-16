n = int(input())


def recursive(num):
    if num == 1:
        return 1
    return num * recursive(num-1)

print(recursive(n))