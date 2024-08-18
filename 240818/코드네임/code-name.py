class codeName():
    def __init__(self, name, score):
        self.name = name
        self.score = score


lst = []
for _ in range(5):
    name, score = input().split()
    lst.append(codeName(name, int(score)))

lst.sort(key=lambda x: x.score)
print(lst[0].name, lst[0].score, end=' ')