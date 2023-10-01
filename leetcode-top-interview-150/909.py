class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        lth = n * n
        dp = [-1] * lth

        board.reverse()

        for i in range(1, n, 2):
            board[i].reverse()

        linearBoard = list(chain(*board))

        def dps(cur, move):
            if dp[cur] == -1 or dp[cur] > move:
                dp[cur] = move
            else:
                return

            if cur == lth - 1:
                return

            for i in range(cur + 1, min(lth, cur + 7)):
                val = linearBoard[i]

                if val == -1:
                    dps(i, move + 1)
                else:
                    dps(val - 1, move + 1)

        dps(0, 0)

        return dp[-1]
