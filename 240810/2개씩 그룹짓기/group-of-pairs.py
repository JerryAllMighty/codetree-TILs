n = int(input())
lst = list(map(int, input().strip().split(' ')))

answer = 10 ** 9
for i in range((2 * n)):
    for j in range(i + 1, (2 * n)):
        # 2개씩 그룹짓고 리스트에 넣어준다
        temp = []
        num1 = lst[i] + lst[j]
        temp.append(num1)
        num2 = 0
        for k in range((2 * n)):

            if k != i and k != j:
                if num2 == 0:
                    num2 += lst[k]
                else:
                    num2 += lst[k]
                    temp.append(num2)
                    num2 = 0

        # 그룹지은 것들 중 최댓값을 찾는다.
        choidae = max(temp)
        # 더 작은 최댓값을 삽입
        if choidae < answer:
            answer = choidae

print(answer)