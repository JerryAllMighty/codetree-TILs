n, m = map(int, input().split(' '))

lst = [
    [0 for i in range(m)]
    for j in range(n)
]
num = -1
for i in range(m):
    if i % 2 == 0:
        for j in range(n):
            num += 1
            lst[j][i] = num
    else:
        for j in range(n - 1, -1, -1):
            num += 1
            lst[j][i] = num

for i in lst:
    print(*i)