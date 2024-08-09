n = int(input())
lst = [
    [0 for i in range(n)]
    for _ in range(n)

]
for i in range(n):
    startCol = i + 1
    for j in range(startCol):
        if i < 1:
            lst[i][j] = 1
            break
        elif j < 1:
            lst[i][j] = 1
            continue
        else:
            one = lst[i - 1][j - 1]
            two = lst[i - 1][j]
            lst[i][j] = one + two

for i in lst:
    answer = []
    for j in range(n):
        if i[j] != 0:
            answer.append(i[j])
    print(*answer)