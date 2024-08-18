class nextLevel():
    def __init__(self, id, level):
        self.id = id
        self.level = level


id, level = input().split()
next = nextLevel('codetree', '10')
next2 = nextLevel(id, level)


print('user ' + next.id + ' lv ' + next.level)
print('user ' + next2.id + ' lv ' + next2.level)