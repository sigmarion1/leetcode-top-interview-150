class Solution:
    def __init__(self):
        self.parentheses = {"(": ")", "{": "}", "[": "]"}

    def isValid(self, s: str) -> bool:
        return self.recursiveIsValid(s, [])

    def recursiveIsValid(self, s, stack) -> bool:
        if not s:
            return False

        cur = s[0]

        if cur in self.parentheses:
            if len(s) == 1:
                return False
            return self.recursiveIsValid(s[1:], stack + [cur])

        if not stack:
            return False

        if self.parentheses.get(stack[-1]) == cur:
            if len(s) == 1 and len(stack) == 1:
                return True
            else:
                return self.recursiveIsValid(s[1:], stack[:-1])

        return False
