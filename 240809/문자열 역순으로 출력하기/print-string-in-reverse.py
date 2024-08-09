lst = []
for _ in range(4):
    s = input()
    lst.append(s)

for i in range(len(lst) - 1, -1, -1):
    print(lst[i])