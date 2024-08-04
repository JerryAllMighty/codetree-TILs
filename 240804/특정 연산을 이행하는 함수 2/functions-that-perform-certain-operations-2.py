import math

lst = list(map(float, input().split(' ')))
small = min(lst)
big = max(lst)
mid = [i for i in lst if i is not small and i is not big]

print(math.ceil(big), math.floor(small), round(mid[0]), sep=' ')