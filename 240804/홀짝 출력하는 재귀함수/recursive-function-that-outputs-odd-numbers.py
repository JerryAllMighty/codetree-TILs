n = int(input())
lst = []
if n % 2 == 0:
    for i in range(2,n+1,2):
        lst.append(i)
else:
    for i in range(1, n + 1,2):
        lst.append(i)
print(*lst)