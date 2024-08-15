n,m = map(int, input().split())

lst = [
    list(input().split())
    for _ in range(n)
]
answer = 0
for i in range(n):
    for j in range(n):
        for k in range(i+1, n):
            for l in range(j + 1, n):
                if lst[i][j] != lst[k][l]:
                    answer += 1
                    lst[k][l] = lst[i][j]


print(answer)