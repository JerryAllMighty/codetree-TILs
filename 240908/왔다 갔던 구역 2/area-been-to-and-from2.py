n = int(input())

lst = [0 for _ in range(201)]

current = 0
lastDirection = ''
for _ in range(n):
    cnt, direction = input().split()
    if lastDirection == 'R':
        if direction == 'L':
            current -= 1
    elif lastDirection == 'L':
        if direction == 'R':
            current += 1

    for i in range(int(cnt)):
        if direction == 'R':
            lst[100 + current] += 1
            current += 1
        else:
            lst[100 + current] += 1
            current -= 1

    lastDirection = direction

print(len([i for i in lst if i >= 2]))