a, b, x, y = map(int, input().split())
q=y-x
w=x-a+y-b
e=x-a+y-x
r=a-x+b-y
if q < 0:
    q=100 ** 4
if w < 0:
    w = 100 ** 4
if e < 0:
    e = 100 ** 4
if r < 0:
    r = 100 ** 4
print(min(q,w,e,r))