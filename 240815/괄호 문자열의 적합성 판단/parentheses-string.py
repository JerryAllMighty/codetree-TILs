# class Stack():
#     def __init__(self):
#         self.items = []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         if len(self.items) < 1:
#             return Exception("Stack is empty")
#         return self.items.pop()
#
#     def size(self):
#         return len(self.items)
#
#     def empty(self): return 1 if not self.items else 0
#
#     def top(self): return self.items[-1]


s = input()
lst = []
for i in s:
    if i == '(':
        lst.append(i)
    elif i == ')':
        if len(lst) > 0:
            lst.pop()
print('Yes' if len(lst) == 0 else 'No')