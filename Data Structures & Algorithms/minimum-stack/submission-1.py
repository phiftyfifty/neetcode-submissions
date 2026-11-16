class MinStack:
    def __init__(self):
        self.stack = []
    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append([val, min(val, self.stack[-1][1])])
        else:
            self.stack.append([val, val])

    def pop(self) -> None:
        if not self.stack:
            raise ValueError("stack should not be empty when popping.")
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            raise ValueError("stack cannot be peaked when finding the top of the stack.")
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            raise ValueError("cannot find min when stack is empty.")
        return self.stack[-1][1]
        
