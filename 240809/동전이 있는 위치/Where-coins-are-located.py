n, m = map(int, input().split(' '))
lst = [
    [0 for i in range(n)]
    for _ in range(n)
]

for i in range(m):
    r,c = map(int, input().split(' '))
    lst[r-1][c-1] = 1

for i in lst:
    print(*i)