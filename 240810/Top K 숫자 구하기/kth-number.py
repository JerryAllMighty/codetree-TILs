n, k = map(int, input().strip().split(' '))

arr = list(map(int, input().strip().split(' ')))
arr.sort()

print(arr[int(k) - 1])