n = int(input())

lst = list(map(int, input().strip().split(' ')))

cmp1 = 10 ** 9
# 2개씩 그룹을 짝짓는다
for i in range((2*n)-2):
    for j in range(i+1, (2 * n)):
        # 짝지은 그룹들의 합은 보관하는 리스트
        temp = []
        temp.append(lst[i]+lst[j])
        num = 0
        for k in range(0, (2 * n)):
            if k != i and k != j:
                if num == 0:
                    num += lst[k]
                else:
                    num += lst[k]
                    temp.append(num)
                    num = 0

        # 짝지은 그룹 중 최댓값을 찾는다
        if max(temp) < cmp1:
            # 그중 최솟값을 삽입
            cmp1 = max(temp)
print(cmp1)