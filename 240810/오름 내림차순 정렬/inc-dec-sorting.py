n = int(input())

lst = list(map(int, input().split(' ')))
lst.sort()
print(*lst)
lst.sort(reverse=True)
print(*lst)