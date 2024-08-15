lst = input().split()
a = int(lst[0])
b = int(lst[1])
answer = 0


def isPrimeNum(num):
    isPrime = True
    if num < 1:
        return False
    else:
        for j in range(2, num):
            if num % j == 0:
                isPrime = False
    return isPrime


for i in range(a, b + 1):
    if isPrimeNum(i):
        answer += i

print(answer)