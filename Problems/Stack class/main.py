class Stack:

    def __init__(self):
        self._stack = []

    def push(self, el):
        self._stack.append(el)

    def pop(self):
        return self._stack.pop()

    def peek(self):
        return self._stack[-1]

    def is_empty(self):
        return not self._stack
