import collections

n = int(input())
lst = [
    ['W' for i in range(200)]
    for _ in range(200)
]
offset = 100
isRed = True
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            if isRed:
                lst[i + offset][j + offset] = 'R'
            else:
                lst[i + offset][j + offset] = 'B'

    if isRed is True:
        isRed = False
    else:
        isRed = True

answer = 0
for i in lst:
    answer += collections.Counter(i).get('B') if collections.Counter(i).get('B') is not None else 0

print(answer)