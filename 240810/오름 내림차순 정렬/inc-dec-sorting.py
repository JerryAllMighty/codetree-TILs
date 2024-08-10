n = int(input())

lst = list(map(int, input().strip().split(' ')))

lst.sort()
print(*lst)
lst.sort(reverse=True)
print(*lst)