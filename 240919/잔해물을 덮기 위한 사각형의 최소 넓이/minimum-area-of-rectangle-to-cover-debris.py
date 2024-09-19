import collections

lst = [
    [0 for i in range(2 * 1000)]
    for _ in range(2 * 1000)
]
offset = 1000
x1, y1, x2, y2 = map(int, input().split())
for i in range(x1, x2+1):
    for j in range(y1, y2+1):
        lst[i][j] = 2

x3, y3, x4, y4 = map(int, input().split())

for i in range(x3, x4+1):
    for j in range(y3, y4+1):
        lst[i][j] -= 1

rows = []
cols = []
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j] == 2:
            rows.append(i)
            cols.append(j)

print((max(rows) - min(rows)) * (max(cols) - min(cols)))