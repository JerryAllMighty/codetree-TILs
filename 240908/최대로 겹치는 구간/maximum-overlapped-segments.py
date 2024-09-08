n = int(input())

lst = [0 for _ in range(201)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x,y):
        lst[100 + i] += 1

print(max(lst))