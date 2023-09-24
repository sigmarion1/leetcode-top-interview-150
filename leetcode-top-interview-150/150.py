class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import math

        optrs = ("+", "-", "*", "/")

        def op(a: int, b: int, c: str):
            if c == "+":
                return a + b
            if c == "-":
                return a - b
            if c == "*":
                return a * b
            if c == "/":
                return math.trunc(a / b)

        stack = []
        for token in tokens:
            if token in optrs:
                last = stack.pop()
                first = stack.pop()
                stack.append(op(first, last, token))
            else:
                stack.append(int(token))

        return stack.pop()
