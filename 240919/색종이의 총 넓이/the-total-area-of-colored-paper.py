import collections

n = int(input())
lst = [
    [0 for i in range(n * 8)]
    for _ in range(n * 8)
]
cnt = n
while (cnt > 0):
    x, y = map(int, input().split())
    for i in range(x, x + 8):
        for j in range(y, y + 8):
            lst[i][j] = 1
    cnt -= 1
answer = 0
for i in lst:
    answer += collections.Counter(i).get(1) if collections.Counter(i).get(1) is not None else 0

print(answer)