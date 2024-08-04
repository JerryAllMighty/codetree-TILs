n = int(input())
lst = [
    [0 for i in range(n)]
    for _ in range(n)
]
num = 0
for i in range(n):
    for j in range(n):
        num+=1
        lst[j][i] = num

for k in lst:
    print(*k)