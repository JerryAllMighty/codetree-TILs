n = int(input())
lst = list(map(int, input().split()))
answers = [lst[0]]
for i in range(1,n):
    key = lst[i]
    for j in range(len(answers)-1, -1, -1):
        if answers[j] < key:
            answers.insert(j+1,key)
            break
    if answers[0] > key:
            answers.insert(0, key)

print(*answers)