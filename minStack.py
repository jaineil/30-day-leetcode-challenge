# Used the classic 2 stack solution. 
# One to hold all the operations and another to hold minimum values.

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.minStack.append(x)
            self.stack.append(x)
        elif x <= self.minStack[-1]:
            self.stack.append(x)
            self.minStack.append(x)
        else:
            self.stack.append(x)

    def pop(self) -> None:
        if self.stack[-1] == self.minStack[-1]:
            self.stack.pop()
            self.minStack.pop()
        else: 
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]