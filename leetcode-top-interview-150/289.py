class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        vect = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                lives = 0

                for dx, dy in vect:
                    x = j + dx
                    y = i + dy

                    if -1 in (x, y) or x == n or y == m:
                        continue

                    if abs(board[y][x]) == 1:
                        lives += 1

                if board[i][j] == 1 and (lives < 2 or lives > 3):
                    board[i][j] = -1
                elif board[i][j] == 0 and lives == 3:
                    board[i][j] = 2

        for i in range(m):
            for j in range(n):
                board[i][j] = 1 if (board[i][j] > 0) else 0
