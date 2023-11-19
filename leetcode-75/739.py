class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i, v in enumerate(temperatures):
            while stack and stack[-1][1] < v:
                index, val = stack.pop()
                ans[index] = i - index
            stack.append([i, v])

        return ans
