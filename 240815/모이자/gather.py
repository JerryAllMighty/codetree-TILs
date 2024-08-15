n = int(input())
lst = list(map(int, input().split()))

answer = 10 ** 9

for i in range(n):
    gather = lst[i]
    cmp = 0
    for j in range(n):
        if j != i:
            cmp += lst[j] * abs(i - j)
    if cmp < answer:
        answer = cmp

print(answer)