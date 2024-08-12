lst = []
for _ in range(10):
    lst.append(input())

k = input()

for s in lst:
    if s[-1] == k:
        print(s)
        exit(0)
print('None')