n = int(input())
lst = list(map(int, input().split()))
answer = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i < j < k and lst[i] <= lst[j] <= lst[k] and lst[i] != lst[j] and lst[i] != lst[k] and lst[j] != lst[k]:
                answer += 1

print(answer)