class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if matrix[i][-1] < target:
                continue

            if matrix[i][0] <= target <= matrix[i][-1]:
                if target in matrix[i]:
                    return True
                else:
                    continue

            return False

        return False
