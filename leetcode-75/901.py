class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        temp_val = 1

        while self.stack and self.stack[-1][0] <= price:
            _, cur_val = self.stack.pop()
            temp_val += cur_val

        self.stack.append((price, temp_val))

        return temp_val


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
