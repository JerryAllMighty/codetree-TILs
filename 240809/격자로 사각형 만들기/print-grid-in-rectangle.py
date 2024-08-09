n = int(input())
lst = [
    [1 for i in range(n)]
    for _ in range(n)
]

for i in range(n):
    for j in range(n):
        if i >= 1 and j >= 1:
            lst[i][j] = lst[i][j-1] + lst[i-1][j-1] + lst[i-1][j]

for i in lst:
    print(*i)