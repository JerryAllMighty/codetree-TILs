class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) < 1:
            return Exception("Stack is empty")
        return self.items.pop()

    def size(self):
        return len(self.items)

    def empty(self): return 1 if not self.items else 0

    def top(self): return self.items[-1]


n = int(input())
stack = Stack()
for _ in range(n):
    cmd = input().split()
    if len(cmd) > 1:
        if cmd[0] == 'push':
            stack.push(cmd[1])
    else:
        if cmd[0] == 'pop':
            print(stack.pop())
        elif cmd[0] == 'empty':
            print(stack.empty())
        elif cmd[0] == 'size':
            print(stack.size())
        elif cmd[0] == 'top':
            print(stack.top())