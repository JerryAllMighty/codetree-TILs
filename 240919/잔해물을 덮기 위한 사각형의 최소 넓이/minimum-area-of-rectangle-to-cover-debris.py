import collections

lst = [
    [0 for i in range(2 * 1000)]
    for _ in range(2 * 1000)
]
offset = 1000
x1, y1, x2, y2 = map(int, input().split())
for i in range(x1, x2):
    for j in range(y1, y2):
        lst[i + offset][j + offset] = 2

x3, y3, x4, y4 = map(int, input().split())

for i in range(x3, x2):
    for j in range(y1,y4):
        lst[i + offset][j + offset] -= 1

answer = 0
first = 0
dup = 0
for i in lst:
    first += collections.Counter(i).get(2) if collections.Counter(i).get(2) is not None else 0
    dup += collections.Counter(i).get(1) if collections.Counter(i).get(1) is not None else 0
if dup > first:
    print(first)
else:
    print(first + dup)