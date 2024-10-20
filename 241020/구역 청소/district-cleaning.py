a, b = map(int, input().split())
c, d = map(int, input().split())

if b <= c:
    print((b - a) + (d - c))
else:
    print(max(b, d) - min(a, c))