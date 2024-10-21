n = int(input())
answer = 0
lst = list(map(int, input().split()))
lst2 = list(map(int, input().split()))


def findSmall(num):
    for i in range(n):
        if lst[i] + num < lst2[i]:
            return i
    return -1


for i in range(len(lst)):
    if lst[i] > lst2[i]:
        gap = lst[i] - lst2[i]
        idx = findSmall(gap)
        answer += (gap * (idx - i))

print(answer)