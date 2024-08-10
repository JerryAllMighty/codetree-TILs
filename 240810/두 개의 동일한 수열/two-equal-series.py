n = int(input())

lst = list(map(int, input().strip().split(' ')))
lst2 = list(map(int, input().strip().split(' ')))

lst.sort()
lst2.sort()

print('Yes' if lst == lst2 else 'No')