a, b, x, y = map(int, input().split())
q=abs(b-a)
w=abs(x-a)+abs(b-y)
e=abs(y-a)+abs(b-x)
print(min(q,w,e))