class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
            new_row = []
            for j in range(n):
                new_row.append(matrix[n - 1 - j][i])
            matrix.append(new_row)

        del matrix[:n]
