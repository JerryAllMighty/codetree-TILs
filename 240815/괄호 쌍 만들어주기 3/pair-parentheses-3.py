s = input()

answer = 0
for i in range(len(s)):
    if s[i:i+1] == '(':
        for j in range(i, len(s)):
            if s[j:j + 1] == ')':
                answer += 1

print(answer)