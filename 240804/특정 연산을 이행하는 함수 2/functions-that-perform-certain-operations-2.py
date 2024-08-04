import math

lst = list(map(float, input().split(' ')))
small = min(lst)
big = max(lst)
answers = []
for i in lst:
    if i == small:
        answers.append(math.floor(i))
    elif i == big:
        answers.append(math.ceil(i))
    else:
        answers.append(round(i))

print(*answers)