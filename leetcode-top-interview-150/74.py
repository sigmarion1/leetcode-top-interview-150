class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        if m == 1:
            return target in matrix[0]

        for i in range(1, m):
            if target < matrix[i][0]:
                return target in matrix[i - 1]

        return target in matrix[-1]
