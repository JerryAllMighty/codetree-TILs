n = int(input())
answer = 0
length = 0
for _ in range(n):
    s = input()
    if s[0] == 'a':
        answer += 1
    length += len(s)

print(*[length, answer])