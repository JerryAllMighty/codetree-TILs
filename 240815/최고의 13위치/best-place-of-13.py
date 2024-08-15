n = int(input())
lst = [
    list(map(int, input().split()))
    for _ in range(n)
]
answer = 0
for i in range(n):
    for j in range(n-2):
        answer = max(answer, lst[i][j]+lst[i][j+1]+lst[i][j+2])

print(answer)