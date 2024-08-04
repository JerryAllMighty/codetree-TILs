s = list(input().split(' '))
ss = ''
if len(s[0]) > len(s[1]):
    ss = s[0]
elif len(s[0]) < len(s[1]):
    ss = s[1]
else:
    ss = 'same'
print(ss, max(len(s[0]), len(s[1])))