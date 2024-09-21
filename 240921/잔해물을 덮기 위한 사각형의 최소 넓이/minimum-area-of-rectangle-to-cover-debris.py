import collections

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

lst = [
    [0 for _ in range(4000)]
    for _ in range(4000)
]
offset = 1000
for i in range(x1, x2):
    for j in range(y1, y2):
        lst[i + offset][j + offset] = 2

for i in range(x3, x4):
    for j in range(y3, y4):
        if lst[i + offset][j + offset] == 2:
            lst[i + offset][j + offset] -= 1
isLeft = 0
for i in lst:
    if collections.Counter(i).get(2) is not None:
        isLeft += collections.Counter(i).get(2)
if isLeft == 0:
    print(0)
    exit(1)

a = 0
b = x2 + offset
c = 0
d = y2 + offset
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j] == 2:
            if i > a:
                a = i
            if i < b:
                b = i
            if j > c:
                c = j
            if j < d:
                d = j

print((a - b + 1) * (c - d + 1))