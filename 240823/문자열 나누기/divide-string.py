n = int(input())
lst = ''.join(input().split())
for i in range(0,len(lst),5):
    print(lst[i:i+5])