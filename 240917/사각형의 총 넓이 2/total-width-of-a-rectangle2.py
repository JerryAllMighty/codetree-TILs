import collections

n = int(input())
lst = [
    [0 for _ in range(n * 100)]
    for _ in range(n * 100)
]
offset = 100
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            lst[i + offset][j + offset] = 1
answer = 0
for i in lst:
    answer += collections.Counter(i).get(1) if collections.Counter(i).get(1) is not None else 0

print(answer)