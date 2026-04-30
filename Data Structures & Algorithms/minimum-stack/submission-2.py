class MinStack:

    def __init__(self):
        self.stack = [] # [(val, min_val)]

    def push(self, val: int) -> None:
        if self.stack:
            _, min_val = self.stack[-1]
            if val < min_val:
                min_val = val
            self.stack.append((val, min_val))

        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        print(self.stack)
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
