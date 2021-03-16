
class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        length = self.size()
        return length == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        length = self.size()
        if length:
            return self.stack[-1]
        else:
             return None

    def size(self):
        return len(self.stack)

















