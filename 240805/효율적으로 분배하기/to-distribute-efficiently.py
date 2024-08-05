n = int(input())

answer = 0

answer += (n // 5)
n = n % 5
if n >= 3:
    answer += 2
else:
    answer += 1
print(answer)