class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        max_sz = 0

        while j < m - max_sz:
            while i < n - max_sz:
                if matrix[j][i] == "1":
                    max_sz = max(max_sz, self.makeSquare(i, j, matrix, max_sz))
                i += 1
            j += 1
            i = 0

        return max_sz**2

    def makeSquare(self, x, y, matrix, max_sz):
        m, n = len(matrix), len(matrix[0])
        possible_sz = min(m - y, n - x)

        for k in range(0, possible_sz + 1):
            for i in range(0, k):
                if "0" in (matrix[y + i][x + (k - 1)], matrix[y + (k - 1)][x + i]):
                    return k - 1

        return possible_sz
