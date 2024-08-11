# n = int(input())
# lst = list(map(int, input().split()))
#
#
# # 각각의 정렬된 리스트로 나누는 과정
# def divide(arr, left, right):
#     if left < right:
#         mid = (left + right) // 2
#         divide(arr, left, mid)
#         divide(arr, mid+1, right)
#         merge(arr, left, mid, right)
#
#
#
# # 나뉜 정렬 리스트를 합치는 과정
# def merge(arr, left, mid, right):
#     tempLst=  []
#     arrTempLst = [arr[i] for i in arr(left, right+1)]
#     while():
#
#
#     idx = left
#     for i in tempLst:
#         arr[idx] = i
#         idx += 1
#
#
# divide(lst, 0, n-1)


n, k = map(int, input().strip().split(' '))
lst = list(map(int, input().strip().split(' ')))
answer = n
bFlag = False

for i in range(n):
    num = lst[i]
    j = i + 1
    while (j < n):
        if num + lst[j] >= k:
            bFlag = True
            if (j - i) < answer:
                answer = j - i + 1
        j += 1
if bFlag:
    print(answer)
else:
    print(-1)