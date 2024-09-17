import collections

a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = list(map(int, input().split()))
lst = [
    [0 for i in range(1000 * 3)]
    for _ in range(1000 * 3)
]
offset = 1000
x1, y1, x2, y2 = a[0], a[1], a[2], a[3]
for i in range(x1, x2):
    for j in range(y1, y2):
        lst[i + offset][j + offset] = 2

bx1, by1, bx2, by2 = b[0], b[1], b[2], b[3]
for i in range(bx1, bx2):
    for j in range(by1, by2):
        lst[i + offset][j + offset] = 2

mx1, my1, mx2, my2 = m[0], m[1], m[2], m[3]
for i in range(mx1, mx2):
    for j in range(my1, my2):
        lst[i + offset][j + offset] -= 1
answer = 0
for i in lst:
    answer += collections.Counter(i).get(2) if collections.Counter(i).get(2) is not None else 0

print(answer)