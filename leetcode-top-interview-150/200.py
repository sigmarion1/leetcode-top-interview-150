class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(x, y):
            if not 0 <= x < n or not 0 <= y < m or grid[y][x] != "1":
                return

            grid[y][x] = "#"
            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x - 1, y)
            dfs(x, y - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(j, i)
        return count
