class info():
    def __init__(self, name, bg, location):
        self.name = name
        self.bg = bg
        self.location = location


n = int(input())
lst = []
for _ in range(n):
    each = input().split()
    one = info(each[0], each[1], each[2])
    lst.append(one)

lst.sort(key=lambda x: x.name, reverse=True)
print('name ' + lst[0].name)
print('addr ' + lst[0].bg)
print('city ' + lst[0].location)