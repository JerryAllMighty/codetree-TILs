class bomb():
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second


code, color, second = input().split()
one = bomb(code, color, second)
print('code : ' + one.code)
print('color : ' + one.color)
print('second : ' + one.second)