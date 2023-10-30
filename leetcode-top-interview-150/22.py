class Solution:
    def recursive(self, start, end, s):
        if start == 0 and end == 0:
            return [s]

        results = []

        if start:
            results += self.recursive(start - 1, end, s + "(")
        if start < end:
            results += self.recursive(start, end - 1, s + ")")

        return results

    def generateParenthesis(self, n: int) -> List[str]:
        start = n - 1
        end = n

        return self.recursive(start, end, "(")
