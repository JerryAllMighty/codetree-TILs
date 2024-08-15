lst = input().split()
a = int(lst[0])
b = int(lst[1])
answer = 0
for i in range(a, b+1):
   isPrime = True
   for j in range(2,i):
      if i % j == 0:
         isPrime = False

   if isPrime is True:
      answer += i

print(answer)