n = int(input())
answer = -1
tempMok = n // 5
while (tempMok >= 0):
    tempNmg = ((n - (tempMok * 5)) % 3)
    if tempNmg == 0:
        answer = tempMok + ((n - (tempMok * 5)) // 3)
        break
    else:
        tempMok -= 1

print(answer)