n = int(input())
lst = []
for i in range(n):
    arriveTime, dueTime = map(int, input().split(' '))
    lst.append([arriveTime, dueTime])
answer = lst[0][0]
lst.sort(key=lambda x:x[0])
for idx in range(len(lst)):
    if answer < lst[idx][0]:
        answer = lst[idx][0]
    answer += lst[idx][1]

print(answer)