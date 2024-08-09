s = input()
lst = ["apple", "banana", "grape", "blueberry", "orange"]

answer = 0
for i in lst:
    if i[2] == s or i[3] == s:
       print(i)
       answer += 1

print(answer)