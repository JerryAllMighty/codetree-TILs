n = int(input())
temp = []
for _ in range(n):
    a, b = map(int, input().split())
    temp.append([i for i in range(a,b+1)])

answer = 'Yes'
def isIn(lst1,lst2):
    for i in lst1:
        if i in lst2:
            return True
    return False

for i in range(n-1):
    for j in range(i+1,n):
        if isIn(temp[i], temp[j]) is False:
            answer = 'No'
print(answer)