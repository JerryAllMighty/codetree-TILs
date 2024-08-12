lst = []
for _ in range(10):
    lst.append(input())

k = input()
bFlag = False
for s in lst:
    if s[-1] == k:
        bFlag = True
        print(s)
if bFlag == False:
    print('None')