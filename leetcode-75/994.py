class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))

        fresh = 0
        rotten = 0
        first = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten += 1
                    first.append((i, j))

        if fresh == 0:
            return 0

        q = deque()
        q.append(first)

        minute = -1

        while q:
            minute += 1

            cur = q.popleft()
            nextRotten = []

            for i, j in cur:
                for di, dj in dirs:
                    if (
                        0 <= i + di < m
                        and 0 <= j + dj < n
                        and grid[i + di][j + dj] == 1
                    ):
                        grid[i + di][j + dj] = 2
                        nextRotten.append((i + di, j + dj))
                        rotten += 1
                        fresh -= 1

            if nextRotten:
                q.append(nextRotten)

        if fresh:
            return -1

        return minute
