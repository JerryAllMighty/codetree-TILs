n = int(input())
lst = [0 for i in range(1000)]
for _ in range(n):
    start, end, cnt = map(int, input().split())
    for i in range(start, end+1):
        lst[i] += cnt

print(max(lst))