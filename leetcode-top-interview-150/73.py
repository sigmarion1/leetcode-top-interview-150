class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m, n = len(matrix), len(matrix[0])
        row, col = set(), set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)

        for i in row:
            matrix[i] = [0] * n

        for i in range(m):
            if i in row:
                continue
            for j in col:
                matrix[i][j] = 0
