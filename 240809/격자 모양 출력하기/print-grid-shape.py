n, m = map(int, input().split(' '))
lst = [
    [0 for i in range(n)]
    for _ in range(n)
]

for i in range(m):
    r, c = map(int, input().split(' '))
    lst[r - 1][c - 1] = r * c

for j in lst:
    print(*j)