n = int(input())
answer = 0
lst = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

for i in range(n):
    if lst[i] > lst2[i]:
        gap = lst[i] - lst2[i]
        lst[i+1] += gap
        lst[i] -= gap
        answer += gap

print(answer)