n = input()

print('Yes' if int(n) % 2 == 0 and sum(list(map(int,n))) % 5 == 0 else 'No')