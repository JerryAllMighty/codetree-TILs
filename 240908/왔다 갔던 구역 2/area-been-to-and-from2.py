n = int(input())

lst = [0 for _ in range(201)]

current = 0
for _ in range(n):
    cnt, direction = input().split()
    for i in range(int(cnt)):
        idx = 100 + current
        if idx > 200:
            idx = 200
        lst[idx] += 1
        if direction == 'R':
            current += 1
        else:
            current -= 1

print(len([i for i in lst if i >= 2]))