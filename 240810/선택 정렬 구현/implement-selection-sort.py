import sys
n = int(input())
lst = list(map(int, input().split()))



for i in range(n):
    minimum = sys.maxsize
    idx = 0
    for j in range(i,n):
        if lst[j] < minimum:
            minimum = lst[j]
            idx = j

    lst[i], lst[idx] = lst[idx], lst[i]

print(*lst)