n, k, word = input().split()
n = int(n)
k = int(k)

lst = [
    input()
    for _ in range(n)
]
wordLst = []
for s in lst:
    if s[:2] == word:
        wordLst.append(s)
wordLst.sort()
print(wordLst[k-1])