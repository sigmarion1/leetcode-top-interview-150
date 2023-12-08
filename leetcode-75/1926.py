class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])

        history = set()

        q = deque()

        q.append((0, entrance[1], entrance[0]))

        while q:
            cnt, x, y = q.popleft()

            if y < 0 or y > m - 1 or x < 0 or x > n - 1:
                continue

            if (x, y) in history:
                continue

            history.add((x, y))

            if maze[y][x] == "+":
                continue

            if cnt != 0 and (y == 0 or y == m - 1 or x == 0 or x == n - 1):
                return cnt

            q.append((cnt + 1, x + 1, y))
            q.append((cnt + 1, x, y + 1))
            q.append((cnt + 1, x - 1, y))
            q.append((cnt + 1, x, y - 1))

        return -1
