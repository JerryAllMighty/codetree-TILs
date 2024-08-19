class bomb():
    def __init__(self, name, code):
        self.name = name
        self.code = code


name, code = input().split()
one = bomb(name, code)
two = bomb('codetree', '50')
print('product ' + two.code + ' is ' + two.name)
print('product ' + one.code + ' is ' + one.name)