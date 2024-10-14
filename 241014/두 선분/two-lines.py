x1, x2, x3, x4 = map(int, input().split())

print('intersecting' if (x2 >= x3 and x1 <= x4) else 'nonintersecting')