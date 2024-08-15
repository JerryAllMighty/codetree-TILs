s = input()
lst = []
for i in s:
    if i == '(':
        lst.append(i)
    elif i == ')':
        lst.pop()
print('Yes' if len(lst) == 0 else 'No')