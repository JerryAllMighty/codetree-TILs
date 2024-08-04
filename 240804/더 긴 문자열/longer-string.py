s = list(input().split(' '))
ss = ''
if len(s[0]) > len(s[1]):
    ss = s[0]
else:
    ss = s[1]
print(ss, max(len(s[0]), len(s[1])))