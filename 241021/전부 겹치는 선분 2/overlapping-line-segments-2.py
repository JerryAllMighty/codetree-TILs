n = int(input())
temp = []
for _ in range(n):
    a, b = map(int, input().split())
    temp.append([i for i in range(a,b+1)])

answer = 'No'
def isIn(lst1,lst2):
    for i in lst1:
        if i in lst2:
            return True
    return False

def removeEach(idx):
    result = 'Yes'
    lst = []
    for i in range(n):
        if i != idx:
            lst.append(temp[i])

    for i in range(n - 2):
        for j in range(i + 1, n-1):
            if isIn(lst[i], lst[j]) is False:
                result = 'No'

    return result

for i in range(n):
    if removeEach(i) == 'Yes':
        answer = 'Yes'
        break

print(answer)