n = int(input())

lst = [0 for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x,y+1):
        lst[i] += 1

print(max(lst))