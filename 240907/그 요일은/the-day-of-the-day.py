m1, d1, m2, d2 = map(int, input().split())
weekDay = input()
lst = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
days = 0

def countDays(month):
    result = 0
    if month in [1, 3, 5, 7, 8, 10, 12]:
        result += 31
    elif month == 2:
        result += 29
    else:
        result += 30
    return result


for i in range(m1, m2):
    days += countDays(i)

days = days - (d1+lst.index(weekDay)-1) + d2

print((days//7)+1)