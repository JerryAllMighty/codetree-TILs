n,m,k = map(int, input().split(' '))

s = str(n*m*k)
answerS = ''
for i in s:
    if i != '0':
        answerS += i
answer = 1
for s in answerS:
    answer = answer * int(s)
print(answer)