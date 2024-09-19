import collections

lst = [
    [0 for i in range(2 * 1000)]
    for _ in range(2 * 1000)
]
offset = 1000
x1, y1, x2, y2 = map(int, input().split())
for i in range(x1, x2 + 1):
    for j in range(y1, y2 + 1):
        lst[i + offset][j + offset] = 2

x3, y3, x4, y4 = map(int, input().split())

for i in range(x3, x4 + 1):
    for j in range(y3, y4 + 1):
        lst[i + offset][j + offset] -= 1

rows = []
cols = []
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j] == 2:
            rows.append(i)
            cols.append(j)
maxRow = max(rows) if rows else 0
minRow = min(rows) if rows else 0
maxCol = max(cols) if cols else 0
minCol = min(cols) if cols else 0
print((maxRow - minRow) * (maxCol - minCol))