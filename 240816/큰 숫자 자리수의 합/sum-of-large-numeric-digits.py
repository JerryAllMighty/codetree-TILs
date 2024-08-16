lst = list(map(int, input().split()))
def recursive(numLst,idx):
    if idx == len(lst)-1:
        return numLst[idx]
    return numLst[idx] * recursive(numLst,idx+1)

def recursive2(num):
    if num < 10:
        return num
    return recursive2(num//10) + num % 10



print(recursive2(recursive(lst,0)))