n = int(input())

visited = []
lst = []
answer = 0
for _ in range(n):
    pigeon, direction = map(int, input().split())
    if pigeon not in visited:
        visited.append(pigeon)
        lst.append([pigeon, direction])
    else:
        for i in range(len(lst)):
            if lst[i][0] == pigeon and lst[i][1] != direction:
                lst[i][1] = direction
                answer += 1


print(answer)