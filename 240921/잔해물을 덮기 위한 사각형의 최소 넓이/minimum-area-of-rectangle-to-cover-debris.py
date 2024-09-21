x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

lst = [
    [0 for _ in range(4000)]
    for _ in range(4000)
]
offset = 1000
rows = []
cols = []

for i in range(x1, x2 + 1):
    for j in range(y1, y2 + 1):
        rows.append(i)
        cols.append(j)
        lst[i + offset][j + offset] = 2

for i in range(x3, x4 + 1):
    for j in range(y3, y4 + 1):
        if lst[i + offset][j + offset] == 2:
            if i in rows:
                rows.remove(i)
            if j in cols:
                cols.remove(j)
        lst[i + offset][j + offset] -= 1
maxRow = max(rows) if max(rows) is not None else 0
minRow = min(rows) if min(rows) is not None else 0
maxCol = max(cols) if max(cols) is not None else 0
minCol = min(cols) if min(cols) is not None else 0

print((maxRow - minRow) * (maxCol - minCol))