lst = [
    input().split(' ')
    for _ in range(3)
]
input()
lst2 = [
    input().split(' ')
    for _ in range(3)
]
for i in range(3):
    num1 = 0
    num2 = 0
    for j in range(3):
        num1 = int(lst[i][j])
        num2 = int(lst2[i][j])

        print(num1 * num2, end=' ')

    print()