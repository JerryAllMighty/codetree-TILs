lst = input().split()
a = int(lst[0])
b = int(lst[1])
answer = 0
for i in range(a, b+1):
    s = str(i)
    if '3' in s or '6' in s or '9' in s or i % 3 == 0:
        answer += 1

print(answer)