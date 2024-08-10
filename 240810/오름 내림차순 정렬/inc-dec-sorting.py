n = int(input())

lst2 = input().split(' ')
lst = []
for i in lst2:
    lst.append(int(i))

lst.sort()
print(*lst)
lst.sort(reverse=True)
print(*lst)