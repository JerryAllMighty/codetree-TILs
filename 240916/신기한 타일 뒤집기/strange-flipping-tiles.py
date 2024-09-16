import collections

n = int(input())

lst = ['C' for i in range(100 * n)]
current = 0
for i in range(n):
    cnt, direction = input().split()
    cnt = int(cnt)
    while(cnt > 0):
        if direction == 'R':
            lst[current] = 'B'
            current += 1
        elif direction == 'L':
            lst[current] = 'W'
            current -= 1

        cnt -= 1
    if direction == 'R':
        current -= 1
    elif direction == 'L':
        current += 1

w = collections.Counter(lst).get('W') if collections.Counter(lst).get('W') is not None else 0
b = collections.Counter(lst).get('B') if collections.Counter(lst).get('B') is not None else 0
print(w, b)