class StockSpanner:

    def __init__(self):
        self.stack = [] # [(temp, index)]
        self.index = 0

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        self.index+=1
        removed_val = 1
        if self.stack:
            removed_val = self.index - self.stack[-1][1]
        else:
            removed_val = self.index
        self.stack.append((price, self.index))
        return removed_val


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)