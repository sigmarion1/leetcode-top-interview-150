class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])

        if n < 1:
            return []

        result = []

        if m == 1:
            return matrix[0]
        elif n == 1:
            for row in matrix:
                result.append(row[0])
            return result

        result += matrix[0]
        del matrix[0]

        for i in range(len(matrix)):
            result.append(matrix[i][-1])
            del matrix[i][-1]

        result += reversed(matrix[-1])
        del matrix[-1]

        for i in range(len(matrix) - 1, -1, -1):
            result.append(matrix[i][0])
            del matrix[i][0]

        result += self.spiralOrder(matrix)

        return result
