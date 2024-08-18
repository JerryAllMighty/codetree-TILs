import sys
sys.setrecursionlimit(10000)

n = int(input())
given = list(map(int, input().split()))
lst = []
answer = 1


def recursive(num, cmp):
    if cmp == 1:
        return lst.append(cmp)
    if num % cmp == 0:
        lst.append(cmp)
    return recursive(num, cmp - 1)


def recursive2(num, idx):
    if idx > n - 1:
        return 1
    # 두 수의 최소공배수를 구한다
    # 구한 최소공배수와 다음 수의 최소공배수를 구해서 answer를 갱신해준다
    global lst
    lst = []
    recursive(num, num)
    recursive(given[idx], given[idx])
    maxYaksu = 1
    for i in lst:
        if lst.count(i) > 1 and i > maxYaksu:
            maxYaksu = i
    minBaesu = maxYaksu * (num // maxYaksu) * (given[idx] // maxYaksu)
    recursive2(minBaesu, idx + 1)
    if idx == n - 1:
        global answer
        answer = minBaesu
    return


recursive2(given[0], 1)
print(answer)