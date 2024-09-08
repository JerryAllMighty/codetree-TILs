import collections
n,k = map(int, input().split())
lst = [0 for _ in range(n)]

for _ in range(k):
    a,b = map(int, input().split())
    for i in range(a,b+1):
        lst[i-1] += 1


print(max(lst))