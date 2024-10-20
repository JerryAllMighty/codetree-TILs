n = int(input())

a, b = map(int, input().split())
temp = [i for i in range(a, b + 1)]
cnt = 1
for _ in range(n-1):
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        if i in temp:
            cnt += 1
            break
        temp.append(i)

print('Yes') if n == cnt else print('No')