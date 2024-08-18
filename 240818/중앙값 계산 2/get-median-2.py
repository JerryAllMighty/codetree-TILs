n = int(input())
lst = list(map(int, input().split()))
cmp = []
for i in range(n):
    cmp.append(lst[i])
    if i % 2 == 0:
        cmp.sort()
        print(cmp[i//2],end=' ')