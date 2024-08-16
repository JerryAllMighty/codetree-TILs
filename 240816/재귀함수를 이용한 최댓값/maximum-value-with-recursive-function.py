n = int(input())

lst = list(map(int, input().split()))
def recursive(lst, idx):
    if idx == n - 1:
        return lst[idx]
    return max(lst[idx], recursive(lst, idx + 1))

print(recursive(lst, 0))