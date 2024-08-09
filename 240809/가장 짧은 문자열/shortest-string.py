max = 0
min = 10 ** 9
for _ in range(3):
    s = input()
    if len(s) > max:
        max = len(s)
    if len(s) < min:
        min = len(s)

print(max-min)