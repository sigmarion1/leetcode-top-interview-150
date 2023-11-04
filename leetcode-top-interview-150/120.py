class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            prvRow = triangle[i - 1]
            curRow = triangle[i]
            for i in range(1, len(curRow) - 1):
                curRow[i] = curRow[i] + min(prvRow[i - 1], prvRow[i])
            curRow[0], curRow[-1] = curRow[0] + prvRow[0], curRow[-1] + prvRow[-1]

        return min(triangle[-1])
