class info():
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather


n = int(input())
lst = []
for _ in range(n):
    each = input().split()
    if each[2] == 'Rain':
        lst.append(info(each[0], each[1], each[2]))

lst.sort(key=lambda x: x.date)
print(lst[0].date, lst[0].day, lst[0].weather)