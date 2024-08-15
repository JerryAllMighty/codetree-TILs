n = int(input())
lst = list(map(int, input().split()))
answer = 0
answerList = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if lst[i] <= lst[j] <= lst[k]:
                each = (lst[i],lst[j],lst[k])
                answerList.append(each)

print(len(answerList))