n = int(input())
lst = []
for _ in range(n):
    lst.append(input())
k = input()
cnt = 0
length = 0
for s in lst:
    if s[0:1] == k:
        cnt += 1
        length += len(s)
length = "{:.2f}".format(length//cnt)
print(cnt,length)