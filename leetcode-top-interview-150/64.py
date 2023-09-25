class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid[0]), len(grid)

        memo = [[0] * m for _ in range(n)]

        memo[0][0] = grid[0][0]

        for i in range(0, m - 1):
            memo[0][i + 1] = memo[0][i] + grid[0][i + 1]
        for j in range(0, n - 1):
            memo[j + 1][0] = memo[j][0] + grid[j + 1][0]

        for i in range(0, m - 1):
            for j in range(0, n - 1):
                memo[j + 1][i + 1] = (
                    min(memo[j][i + 1], memo[j + 1][i]) + grid[j + 1][i + 1]
                )

        return memo[n - 1][m - 1]
